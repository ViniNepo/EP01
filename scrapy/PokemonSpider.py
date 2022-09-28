import os
from datetime import time

import scrapy


class PokemonsSpider(scrapy.Spider):
    name = "scrapy"
    currentEvolution = '/pokedex/001.shtml'
    start_urls = ['https://www.serebii.net' + currentEvolution]

    def parse(self, response):

        yield {
            'damage_taken': get_damage(response),
            'next_evolution': get_evolution(response, self.currentEvolution),
            'types': get_types(response),
            'height': response.xpath('//table[@class="dextable"][position()=2]//tr[4]//td[2]//text()').getall()[2].strip(),
            'weight': response.xpath('//table[@class="dextable"][position()=2]//tr[4]//td[3]//text()').getall()[1].strip(),
            'name': response.css('.dextable:nth-child(5) tr:nth-child(2) .fooinfo:nth-child(1) ::text').get(),
            'number': response.css('tr:nth-child(2) .fooinfo~ .fooinfo+ .fooinfo ::text').get()
        }

        nextPage = response.xpath('//table//td[@align="right"]').css('a[href*=pokedex]').xpath('@href').getall()

        if nextPage:
            nextPage = nextPage[0]
            self.currentEvolution = nextPage
            yield scrapy.Request(response.urljoin('https://www.serebii.net' + nextPage))


def get_damage(response):
    damages = []
    for idx, damage in enumerate(response.xpath('//table[@class="dextable"][position()=4]//tr[3]//td//text()').getall()):
        if idx == 0:        damages.append("NORMAL: " + str(damage).replace("*", "").strip())
        elif idx == 1:      damages.append("FIRE: " + str(damage).replace("*", "").strip())
        elif idx == 2:      damages.append("WATER: " + str(damage).replace("*", "").strip())
        elif idx == 3:      damages.append("ELECTRIC: " + str(damage).replace("*", "").strip())
        elif idx == 4:      damages.append("GRASS: " + str(damage).replace("*", "").strip())
        elif idx == 5:      damages.append("ICE: " + str(damage).replace("*", "").strip())
        elif idx == 6:      damages.append("FIGHT: " + str(damage).replace("*", "").strip())
        elif idx == 7:      damages.append("POISON: " + str(damage).replace("*", "").strip())
        elif idx == 8:      damages.append("GROUND: " + str(damage).replace("*", "").strip())
        elif idx == 9:      damages.append("FLYING: " + str(damage).replace("*", "").strip())
        elif idx == 10:     damages.append("PSYCHIC: " + str(damage).replace("*", "").strip())
        elif idx == 11:     damages.append("BUG: " + str(damage).replace("*", "").strip())
        elif idx == 12:     damages.append("ROCK: " + str(damage).replace("*", "").strip())
        elif idx == 13:     damages.append("GHOST: " + str(damage).replace("*", "").strip())
        elif idx == 14:     damages.append("DRAGON: " + str(damage).replace("*", "").strip())
    return damages


def get_evolution(response, currentEvolution):
    nextEvolution = False
    for evo in response.css('.evochain').css('a').xpath('@href').getall():
        if nextEvolution:
            return response.xpath('//table//td[@align="right"]').css('a[href*=pokedex] ::text').getall()[1].strip()
        elif evo == currentEvolution:
            nextEvolution = True


def get_types(response):
    types = []
    for type in response.xpath('//table[@class="dextable"][position()=2]//tr[2]//td[4]//a//@href').getall():
        types.append(type.split('/')[2].split('.')[0])
    return types