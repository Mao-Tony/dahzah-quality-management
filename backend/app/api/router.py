from fastapi import APIRouter

from app.modules.quality import quality_router
from app.modules.quality.deviation_automation_api import router as deviation_automation_router
from app.modules.quality.reagent_api import router as quality_reagent_router
from app.modules.quality.deviation_api import router as deviation_router
from app.platform.system import router as system_router
from app.api.v1.ai_log_api import router as ai_log_router
from app.api.v1.ai_config_api import router as ai_config_router

api_router = APIRouter()

# 系统管理
api_router.include_router(system_router, prefix="/system", tags=["系统"])

# AI日志
api_router.include_router(ai_log_router, prefix="", tags=["AI日志"])

# AI配置
api_router.include_router(ai_config_router, prefix="/ai", tags=["AI配置"])

# 质量管理主页
api_router.include_router(quality_router, prefix="/quality", tags=["质量管理"])

# 偏差管理
api_router.include_router(deviation_router, prefix="/quality", tags=["偏差管理"])

# 偏差报告自动化
api_router.include_router(deviation_automation_router, prefix="/quality", tags=["偏差报告自动化"])

# 质量检验-试剂管理
api_router.include_router(quality_reagent_router, prefix="/quality", tags=["质量检验-试剂管理"])
