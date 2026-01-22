#!/usr/bin/env python3
"""
Servidor HTTP simple con soporte CORS para desarrollo
Este servidor maneja las peticiones mientras Motia no esté disponible
"""
import http.server
import socketserver
import json
import urllib.parse
from datetime import datetime
from typing import Dict, Any

PORT = 8080

class CORSRequestHandler(http.server.SimpleHTTPRequestHandler):
    """Handler HTTP con soporte CORS"""
    
    def end_headers(self):
        """Añade headers CORS a todas las respuestas"""
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type, Authorization')
        self.send_header('Access-Control-Max-Age', '3600')
        super().end_headers()
    
    def do_OPTIONS(self):
        """Maneja preflight requests de CORS"""
        self.send_response(200)
        self.end_headers()
    
    def do_GET(self):
        """Maneja peticiones GET"""
        parsed_path = urllib.parse.urlparse(self.path)
        path = parsed_path.path
        query_params = urllib.parse.parse_qs(parsed_path.query)
        
        # Manejar el endpoint /example
        if path == '/example':
            name = query_params.get('name', ['Mundo'])[0]
            
            response_data = {
                'message': f'Hola, {name}!',
                'timestamp': datetime.utcnow().isoformat() + 'Z',
                'example': True
            }
            
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(response_data).encode('utf-8'))
            return
        
        # Para otras rutas, devolver 404
        self.send_response(404)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        error_response = {'error': 'Not found', 'path': path}
        self.wfile.write(json.dumps(error_response).encode('utf-8'))
    
    def do_POST(self):
        """Maneja peticiones POST"""
        parsed_path = urllib.parse.urlparse(self.path)
        path = parsed_path.path
        
        # Leer el body
        content_length = int(self.headers.get('Content-Length', 0))
        body = self.rfile.read(content_length)
        
        try:
            body_data = json.loads(body.decode('utf-8')) if body else {}
        except json.JSONDecodeError:
            body_data = {}
        
        # Manejar diferentes endpoints POST aquí
        if path == '/example':
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            response_data = {
                'message': 'POST recibido correctamente',
                'data': body_data,
                'timestamp': datetime.utcnow().isoformat() + 'Z'
            }
            self.wfile.write(json.dumps(response_data).encode('utf-8'))
            return
        
        # Para otras rutas, devolver 404
        self.send_response(404)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        error_response = {'error': 'Not found', 'path': path}
        self.wfile.write(json.dumps(error_response).encode('utf-8'))
    
    def log_message(self, format, *args):
        """Personaliza los logs"""
        print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {format % args}")

if __name__ == '__main__':
    with socketserver.TCPServer(("", PORT), CORSRequestHandler) as httpd:
        print(f"🚀 Servidor HTTP con CORS iniciado en http://localhost:{PORT}")
        print(f"📡 Endpoint disponible: GET /example?name=<nombre>")
        print(f"🔒 CORS habilitado para todos los orígenes")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n🛑 Servidor detenido")
            httpd.shutdown()
