from django.contrib import admin
from django.urls import path
from airapp.appviews import create,index,update,delete

urlpatterns = [
    path('pages/airline', index.airline, name='airline'),
    path('pages/crew', index.crew, name='crew'),
    path('pages/journey', index.journey, name='journey'),
    path('pages/risk', index.risk, name='risk'),
    path('pages/traveller', index.traveller, name='traveller'),

    path('pages/airlinecreate', create.createairline, name='creaetairline'),
    path('pages/crewcreate', create.createcrew, name='createcrew'),
    path('pages/journeycreate', create.createjourney, name='createjourney'),
    path('pages/riskcreate', create.createrisk, name='createrisk'),
    path('pages/travellercreate', create.createtraveller, name='createtraveller'),

    path('pages/airstore', create.airlinestore, name='storeair'),
    path('pages/crewstore', create.crewstore, name='storecrew'),
    path('pages/journeystore', create.journeystore, name='storejourney'),
    path('pages/riskstore', create.riskstore, name='storerisk'),
    path('pages/travellerstore', create.travellerstore, name='storetraveller'),

    path('pages/editair/<int:pk>', update.airlineedit, name='airedit'),
    path('pages/editcrew/<int:pk>', update.creweidt, name='creweidt'),
    path('pages/editjourney/<int:pk>', update.journeyedit, name='journeyeidt'),
    path('pages/editrisk/<int:pk>', update.riskedit, name='riskeidt'),
    path('pages/edittraveller/<int:pk>', update.travelleredit, name='travelleredit'),

    path('pages/updateair/<int:pk>', update.airlineupdate, name='airupdate'),
    path('pages/updatecrew/<int:pk>', update.crewupdate, name='crewupdate'),
    path('pages/updatejourney/<int:pk>', update.journeyupdate, name='journeyupdate'),
    path('pages/updaterisk/<int:pk>', update.riskupdate, name='riskupdate'),
    path('pages/updatetraveller/<int:pk>', update.travellerupdate, name='travellerupdate'),

    path('pages/crewdelete/<int:pk>', delete.crewdelete, name='deletecrew'),
    path('pages/airlinedelet/<int:pk>', delete.airlinedelete, name='deleteairline'),
    path('pages/homedelete/<int:pk>', delete.travellerdelete, name='deletetraveller'),
    path('pages/journeydelete/<int:pk>', delete.journeydelete, name='deletejourney'),
    path('pages/riskdelete/<int:pk>', delete.riskdelete, name='deleterisk')
]