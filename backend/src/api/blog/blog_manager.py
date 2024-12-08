from src.api.articles.schemas import CreateSimpleArticleSchema
from src.api.db.models import SimpleArticle
from sqlmodel import Session

class ArticleManager():
    

    def create_simple_article(self, article_data: CreateSimpleArticleSchema, session: Session):
        article = SimpleArticle(**article_data.dict())
        
        session.add(article)
        session.commit()
        session.refresh(article)
        return article
    
    def get_all_articles(self, session: Session):
        pass 
    
    def get_article_by_id(self, article_id: int, session: Session):
        pass 

    def update_article(self, article_id: int, session: Session):
        pass

    def delete_article(self, article_id: int, session: Session):
        pass
