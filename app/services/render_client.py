# app/services/render_client.py
import asyncio
from typing import Dict
from .higgsfield_client import create_talking_head_job, get_job, HiggsfieldError

async def render_with_higgsfield(*, script_id: int, text: str, preset_id: str, duration_s: int, locale: str) -> Dict[str, str]:
    job = await create_talking_head_job(
        script_text=text,
        preset=preset_id,
        duration_s=duration_s,
        locale=locale,
        webhook_url=None  # or your public https webhook endpoint if you have it
    )
    job_id = job.get("job_id") or job.get("id")
    if not job_id:
        raise HiggsfieldError("No job_id in response")

    # Simple polling loop
    for _ in range(60):  # ~ up to N*sleep seconds
        info = await get_job(job_id)
        status = info.get("status")
        if status in ("completed", "done", "succeeded"):
            assets = info.get("assets", {})
            return {
                "video_url": assets.get("video_url") or "",
                "thumb_url": assets.get("thumb_url") or "",
            }
        if status in ("failed", "error"):
            raise HiggsfieldError(f"Higgsfield job failed: {info}")
        await asyncio.sleep(2)

    raise HiggsfieldError("Polling timeout")
