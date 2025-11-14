# src/notion/client.py
import os
from notion_client import Client

class NotionClient:
    def __init__(self):
        self.token = os.getenv('NOTION_TOKEN')
        self.database_id = os.getenv('NOTION_DATABASE_ID')
        
        if not self.token or not self.database_id:
            raise ValueError("NOTION_TOKEN e NOTION_DATABASE_ID devem estar configurados")
            
        self.client = Client(auth=self.token)
    
    def add_job(self, job):
        """Adiciona uma vaga ao database do Notion"""
        try:
            self.client.pages.create(
                parent={"database_id": self.database_id},
                properties={
                    "Vaga": {"title": [{"text": {"content": job['title']}}]},
                    "Empresa": {"rich_text": [{"text": {"content": job['company']}}]},
                    "Localização": {"rich_text": [{"text": {"content": job.get('location', 'N/A')}}]},
                    "Match": {"number": job['match_score']},
                    "Fonte": {"select": {"name": job['source']}},
                    "Nível": {"select": {"name": job.get('experience_level', 'N/A')}},
                    "URL": {"url": job['url']},
                    "Status": {"select": {"name": "Pendente"}}
                }
            )
            print(f"✅ Vaga '{job['title']}' adicionada ao Notion")
        except Exception as e:
            print(f"❌ Erro ao adicionar vaga '{job['title']}': {e}")
