from typing import Optional,List
from fastapi import  Request
from zq.db.mongodb import AsyncIOMotorClient
from zq.db.db_config import database_name
import pymongo

class Paginate:
    def __init__(self,collection_name,conn:AsyncIOMotorClient,request:Request,limit:int=10,offset:int=0,q:Optional[dict]=None):
        '''initalize the paginator class with limit, offset, count query,query parameters'''
        self.collection_name= collection_name
        self.limit = limit
        self.offset=offset
        self.q=q
        self.request=request
        self.count = None
        self.conn  = conn


    async def get_count(self,ListMethod):
        '''get the count of the present data module'''
        row_object  =  self.conn[database_name][self.collection_name].find(self.q)
        results: List[ListMethod] = []
        async for row in row_object:
            results.append(
                ListMethod(**row)

            )
        self.count = len(results)
        return self.count


    async def get_next_link(self):
        '''get the next link in for pagination'''

        if self.offset + self.limit >= self.count:
            return ""
        return str(
            self.request.url.include_query_params(
                limit=self.limit, offset=self.offset + self.limit
            )
        )
    async def get_previous_link(self):
        '''get the previous link of the pagination'''
        if self.offset <= 0:
            return ""

        if self.offset - self.limit <= 0:
            return str(self.request.url.remove_query_params(keys=["offset"]))

        return str(
            self.request.url.include_query_params(
                limit=self.limit, offset=self.offset - self.limit
            )
        )

    async def get_list(self,ListMethod):
        '''get the data list '''
        result_rows =  self.conn[database_name][self.collection_name].find(self.q).skip(self.offset).limit(self.limit).sort('created_at',pymongo.DESCENDING)
        results: List[ListMethod] = []
        async for row in result_rows:
            results.append(
                ListMethod(**row)

                           )

        return results

