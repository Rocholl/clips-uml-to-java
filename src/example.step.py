"""
Ejemplo de Step de Motia en Python

Este es un template básico que puedes usar como punto de partida
para crear tus propios Steps.
"""
from datetime import datetime

config = {
    'name': 'ExampleStep',
    'type': 'api',  # Tipos disponibles: 'api', 'event', 'workflow'
    'path': '/example',
    'method': 'GET',  # Métodos HTTP: 'GET', 'POST', 'PUT', 'DELETE', etc.
}


async def handler(req, context):
    """
    Handler del Step
    
    Args:
        req: Request object con información de la petición HTTP
            - req.get('body', {}) para POST/PUT requests
            - req.get('query', {}) para query parameters
            - req.get('headers', {}) para headers HTTP
        context: Context object con utilidades
            - context.get('logger') para logging
            - context.get('state') para estado persistente
            - context.get('emit') para emitir eventos
    
    Returns:
        dict: Response con 'status' y 'body'
    """
    try:
        logger = context.get('logger') if context else None
        
        if logger:
            logger.info('Ejemplo de Step ejecutado')
        
        # Ejemplo: Obtener query parameters
        query = req.get('query', {}) if isinstance(req, dict) else {}
        name = query.get('name', 'Mundo')
        
        return {
            'status': 200,
            'body': {
                'message': f'Hola, {name}!',
                'timestamp': datetime.utcnow().isoformat() + 'Z',
                'example': True
            }
        }
    except Exception as error:
        logger = context.get('logger') if context and isinstance(context, dict) else None
        if logger:
            logger.error('Error en el Step', {'error': str(error)})
        return {
            'status': 500,
            'body': {'error': 'Error interno del servidor'}
        }
