import random

from django.shortcuts import render
from django.views import View
from tours.mock import title, subtitle, description, departures, tours


class MainView(View):
    def get(self, request, *args, **kwargs):
        context = {
            "title": title,
            "subtitle": subtitle,
            "description": description,
            "departures": departures,
            "tours": random.sample(list(tours.values()), k=6)
        }

        return render(request, 'tours/index.html', context=context)


class DepartureView(View):
    def get(self, request, departure, *args, **kwargs):
        tours_by_departure = [tour for tour in list(tours.values()) if tour["departure"] == departure]
        tours_prices = [tour["price"] for tour in tours_by_departure]
        tours_nights = [tour["nights"] for tour in tours_by_departure]
        context = {
            "title": title,
            "subtitle": subtitle,
            "description": description,
            "departures": departures,
            "departure": departures[departure],
            "current_departure_key": departure,
            "tours": tours_by_departure,
            "tours_count": len(tours_by_departure),
            "min_price": min(tours_prices),
            "max_price": max(tours_prices),
            "min_nights": min(tours_nights),
            "max_nights": max(tours_nights)
        }

        return render(request, 'tours/departure.html', context=context)


class TourView(View):
    def get(self, request, tour_id, *args, **kwargs):
        tour = tours[tour_id]
        context = {
            "title": title,
            "subtitle": subtitle,
            "description": description,
            "departures": departures,
            "tour": tour,
            "departure": departures[tour["departure"]]
        }

        return render(request, 'tours/tour.html', context=context)
