from typing import Optional, Dict, Any
import httpx
from ..config import settings

class HiggsfieldError(Exception):
    pass

def _headers() -> Dict[str, str]:
    return {
        "Authorization": f"Bearer {settings.HIGGSFIELD_API_KEY}",
        "Content-Type": "application/json",
        "Accept": "application/json",
    }

# Example 1: create a lipsync/talking-head render job
async def create_talking_head_job(
    *, script_text: str, voice_id: str = "female_v1", preset: str = "fast", duration_s: int = 9,
    locale: str = "almaty-ru", webhook_url: Optional[str] = None
) -> Dict[str, Any]:
    payload = {
        "type": "talking_head",
        "inputs": {
            "script": script_text,
            "voice_id": voice_id,
            "locale": locale,
            "duration_s": duration_s,
            "motion_preset": preset,
        },
        "webhook_url": webhook_url,  # optional, if your account supports webhooks
    }
    async with httpx.AsyncClient(base_url=settings.HIGGSFIELD_API_BASE, timeout=60) as client:
        r = await client.post("/v1/jobs", headers=_headers(), json=payload)
        if r.status_code >= 400:
            raise HiggsfieldError(f"create job failed: {r.text}")
        return r.json()  # expected to include job_id

# Example 2: poll job status
async def get_job(job_id: str) -> Dict[str, Any]:
    async with httpx.AsyncClient(base_url=settings.HIGGSFIELD_API_BASE, timeout=30) as client:
        r = await client.get(f"/v1/jobs/{job_id}", headers=_headers())
        if r.status_code >= 400:
            raise HiggsfieldError(f"get job failed: {r.text}")
        return r.json()  # expected: {status, assets:{video_url, thumb_url}, ...}
