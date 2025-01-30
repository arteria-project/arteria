"""
Base routes that should be included in all services
"""
from aiohttp import web
from arteria import __version__

base_routes = web.RouteTableDef()


@base_routes.get("/api/1.0/version")
async def version(request):
    """
    Returns service version in use
    """
    return web.json_response(
        {"version": __version__}
    )
