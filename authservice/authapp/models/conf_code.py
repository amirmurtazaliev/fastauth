from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime
from ..database import Base

class ConfCode(Base):
    __tablename__ = "conf_codes"
    
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    user_email: Mapped[str] = mapped_column(nullable=False, index=True)
    code: Mapped[int] = mapped_column(nullable=False)
    created_at: Mapped[datetime] = mapped_column(default=datetime.now)