from pydantic import BaseModel, Field, StrictStr, StrictFloat, StrictInt
from typing import Optional
from typing import List


class Character(BaseModel):
    education: Optional[StrictStr] = Field(None)
    height: Optional[StrictInt | StrictFloat] = Field(None)
    identity: Optional[StrictStr] = Field(None)
    name: Optional[StrictStr] = Field(None)
    other_aliases: Optional[StrictStr] = Field(None, alias='otherAliases')
    universe: Optional[StrictStr] = Field(None)
    weight: Optional[StrictFloat | StrictStr] = Field(None)


class CharactersResponse(BaseModel):
    result: List[Character] = None


class CharacterResponse(BaseModel):
    result: Optional[Character] = None

class CharacterDeletedResponse(BaseModel):
    result: Optional[StrictStr] = None
