from app.schemas import CreateSimpleBlogPost
from app.schemas import ListSimpleBlogPost
from app.db.models import SimpleBlogPost

from sqlmodel import Session
from sqlmodel import select
from uuid import UUID


class BlogManager:

    def get_all_blog_posts(self, session: Session) -> ListSimpleBlogPost:
        """
        List all blog posts.

        :param session: Session object
        :return: ListSimpleBlogPost object
        """
        statement = select(SimpleBlogPost)
        blog_posts = session.exec(statement).all()
        return blog_posts

    def create_simple_article(
        self, blog_data: CreateSimpleBlogPost, session: Session
    ) -> SimpleBlogPost:
        blog_data_dict = blog_data.model_dump()
        blog_post = SimpleBlogPost(**blog_data_dict)

        session.add(blog_post)
        session.commit()
        session.refresh(blog_post)
        return blog_post

    def get_post_by_id(self, post_id: UUID, session: Session) -> SimpleBlogPost:
        statement = select(SimpleBlogPost).where(SimpleBlogPost.post_id == post_id)
        blog_post = session.exec(statement).first()
        return blog_post

    def get_all_posts(self, session: Session) -> SimpleBlogPost:
        statement = select(SimpleBlogPost)
        blog_posts = session.exec(statement).all()
        return blog_posts

    def delete_post(self, post_id: UUID, session: Session) -> SimpleBlogPost:
        statement = select(SimpleBlogPost).where(SimpleBlogPost.post_id == post_id)
        blog_post = session.exec(statement).first()
        session.delete(blog_post)
        session.commit()
        return blog_post
