# main.py
import os
import sys
from datetime import datetime
from src.scraper.linkedin_scraper import LinkedInScraper
from src.matching.matcher import MatchCalculator
from src.notion.client import NotionClient

def main():
    print(f"🚀 AutoMatch Scraper iniciado - {datetime.now()}")
    
    try:
        # 1. Inicializar clientes
        notion = NotionClient()
        matcher = MatchCalculator()
        
        # 2. Buscar vagas (por enquanto mock)
        print("🔍 Buscando vagas...")
        vagas = get_sample_jobs()  # Mock por enquanto
        
        # 3. Calcular matches
        print("🎯 Calculando matches...")
        vagas_com_match = []
        for vaga in vagas:
            match_score = matcher.calculate_match(vaga)
            vaga['match_score'] = match_score
            if match_score >= 70:  # Filtro mínimo
                vagas_com_match.append(vaga)
        
        # 4. Salvar no Notion
        print("💾 Salvando no Notion...")
        for vaga in vagas_com_match[:5]:  # Limitar a 5 vagas no teste
            notion.add_job(vaga)
        
        print(f"✅ Concluído! {len(vagas_com_match)} vagas relevantes encontradas")
        
    except Exception as e:
        print(f"❌ Erro: {e}")
        sys.exit(1)

def get_sample_jobs():
    """Dados mock para teste - substituir por scraper real depois"""
    return [
        {
            "title": "Python Backend Developer",
            "company": "Tech Startup", 
            "location": "Remoto",
            "description": "Busca-se desenvolvedor Python com experiência em FastAPI e Django",
            "skills": ["Python", "FastAPI", "Django", "PostgreSQL"],
            "experience_level": "Pleno",
            "url": "https://linkedin.com/jobs/view/123",
            "source": "linkedin"
        },
        {
            "title": "Data Scientist",
            "company": "Data Corp",
            "location": "São Paulo", 
            "description": "Vaga para cientista de dados com Python e machine learning",
            "skills": ["Python", "Machine Learning", "Pandas", "SQL"],
            "experience_level": "Sênior",
            "url": "https://github.com/jobs/456",
            "source": "github"
        },
        {
            "title": "React Frontend Developer", 
            "company": "Web Agency",
            "location": "Híbrido",
            "description": "Desenvolvedor React Junior para time de frontend",
            "skills": ["JavaScript", "React", "CSS", "HTML"],
            "experience_level": "Junior", 
            "url": "https://vagas.com/789",
            "source": "vagas"
        }
    ]

if __name__ == "__main__":
    main()
