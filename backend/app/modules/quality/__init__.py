from app.modules.quality.api import router as quality_router
from app.modules.quality.deviation_automation_api import router as deviation_automation_router
from app.modules.quality.reagent_api import router as quality_reagent_router
from app.modules.quality.deviation_api import router as deviation_router

__all__ = [
    "quality_router",
    "deviation_automation_router",
    "quality_reagent_router",
    "deviation_router",
]
