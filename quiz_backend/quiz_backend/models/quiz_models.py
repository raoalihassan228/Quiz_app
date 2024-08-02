
from typing import Optional
from sqlmodel import Field, SQLModel

class Category(SQLModel, table=True):
    category_id: Optional[int] = Field(None, primary_key=True)
    category_name: str
    category_description: str
    
class QuizLevel(SQLModel, table=True):
    quiz_level_id: Optional[int] = Field(None, primary_key=True)
    quiz_level: str
    category_id: int = Field(int, foreign_key="category.category_id")
     
class Quiz(SQLModel, table=True):
    question_id: Optional[int] = Field(None, primary_key=True)
    question: str
    quizlevel_id: int = Field(int, foreign_key="quizlevel.quiz_level_id")
    
class Choice(SQLModel, table=True):
    choice_id: Optional[int] = Field(None, primary_key=True)
    quiz_id: int = Field(int, foreign_key="quiz.question_id")
    choice: str
    status: bool = False
    
      