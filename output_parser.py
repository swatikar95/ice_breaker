from langchain.output_parsers import PydanticOutputParser
from langchain_core.pydantic_v1 import BaseModel, Field
from typing import List

class Summary(BaseModel):
    summary:str = Field(description="summary")
    facts:List[str] = Field(description="interesting facts about them")

    def to_dict(self):
        return {"summary":self.summary,"facts":self.facts}
    
class IceBreaker(BaseModel):
    ice_breakers: List[str] = Field(description="Create ice breakers to open a conversation with the person")

    def to_dict(self):
        return {"ice_breakers":self.ice_breakers}
    
class TopicOfInterest(BaseModel):
    topics_of_interest:List[str] = Field(description="Topics that may interest the person")

    def to_dict(self):
        return {"topics_of_interest":self.topics_of_interest}


summary_parser = PydanticOutputParser(pydantic_object=Summary)
ice_breaker_parser = PydanticOutputParser(pydantic_object=IceBreaker)
topics_of_interest = PydanticOutputParser(pydantic_object=TopicOfInterest)