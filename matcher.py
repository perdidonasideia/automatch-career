# src/matching/matcher.py
class MatchCalculator:
    def __init__(self):
        # Perfil mock - depois virá do usuário
        self.user_profile = {
            "skills": ["Python", "FastAPI", "Django", "PostgreSQL", "Machine Learning"],
            "experience_level": "Pleno",
            "preferred_locations": ["Remoto", "São Paulo"],
            "undesired_skills": ["Java", "PHP"]
        }
    
    def calculate_match(self, job):
        """Calcula score de match entre vaga e perfil"""
        score = 0
        
        # Match de skills (50% do score)
        skills_match = self._calculate_skills_match(job.get('skills', []))
        score += skills_match * 0.5
        
        # Match de experiência (25% do score)
        exp_match = self._calculate_experience_match(job.get('experience_level', ''))
        score += exp_match * 0.25
        
        # Match de localização (25% do score)
        location_match = self._calculate_location_match(job.get('location', ''))
        score += location_match * 0.25
        
        return int(score * 100)
    
    def _calculate_skills_match(self, job_skills):
        if not job_skills:
            return 0.5  # Neutro se não há skills especificadas
            
        matching_skills = set(job_skills) & set(self.user_profile['skills'])
        total_skills = len(set(job_skills))
        
        if total_skills == 0:
            return 0.5
            
        return len(matching_skills) / total_skills
    
    def _calculate_experience_match(self, job_experience):
        levels = {"Junior": 1, "Pleno": 2, "Sênior": 3}
        user_level = levels.get(self.user_profile['experience_level'], 2)
        job_level = levels.get(job_experience, 2)
        
        # Penalizar se a vaga for muito acima do nível
        if job_level > user_level + 1:
            return 0.3
        elif job_level == user_level:
            return 1.0
        else:
            return 0.7
    
    def _calculate_location_match(self, job_location):
        preferred = self.user_profile['preferred_locations']
        if any(loc.lower() in job_location.lower() for loc in preferred):
            return 1.0
        return 0.3
