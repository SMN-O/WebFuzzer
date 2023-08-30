from typing import Optional
from pydantic import BaseModel, constr



class URLDict(BaseModel):
	url: constr(regex=r"^(?:http?:\/\/)[\w.-]+(?:\.[\w\.-]+)+[\w\-\._~:/?#[\]@!\$&'\(\)\*\+,;=.]+$")
	custom_query: Optional[str]
