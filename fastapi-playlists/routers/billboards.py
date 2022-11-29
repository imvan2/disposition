from fastapi import APIRouter, Depends, Response
from typing import List, Optional, Union
import requests
import pprint
import json

from queries.billboards import (
    Error,
    BillboardIn,
    BillboardRepo,
    BillboardOut,
)

router = APIRouter()
# where this file is stored

@router.get("/billboard", response_model = list[BillboardOut])
def get_billboard(
    repo: BillboardRepo = Depends()
):
    url = 'https://billboard-api2.p.rapidapi.com/hot-100?range=1-10&date=2022-11-26'
    headers = {
		'X-RapidAPI-Key': '26ee71e221msh7a38114d41adb77p12c43bjsn8afae6ec2da4',
		'X-RapidAPI-Host': 'billboard-api2.p.rapidapi.com'
	}
    response = requests.get(url, headers=headers)
    Billboard = response.json()
    # print("response:::::", billboard["content"])
    Billboard = Billboard["content"].values()
    bb = list(Billboard)
    cont = []
    for val in bb:
        print("val::::::", val)
        d = val.values()
        cont.append(d)

    result = tuple(cont)

    print("result!!!!!!!!!!!!!", result)
    print("bb::::::::", bb)
    print("bb:TYPE:::::::", type(bb))
    return repo.get_all()

# @router.get("/Billboards", response_model=Union[List[BillboardOut], Error])
# def get_all(
#     repo: BillboardRepo = Depends(),
# ):
#     return repo.get_all()

@router.put("/Billboards/{id}", response_model=Union[BillboardOut, Error])
def update_Billboard(
    id: int,
    Billboard: BillboardIn,
    repo: BillboardRepo = Depends(),
) -> Union[Error, BillboardOut]:
    return repo.update(id, Billboard)
