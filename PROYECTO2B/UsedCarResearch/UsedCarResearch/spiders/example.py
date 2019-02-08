import scrapy
import pandas

nombre_archivo = 'results.csv'


class IntroSpider(scrapy.Spider):
    name = '01_get_information'

    def start_requests(self):
        urls = [
            'https://forowarez.net/forums/cuentas-premium.80/',
            'https://forowarez.net/forums/cuentas-premium.80/page-2',
            'https://forowarez.net/forums/cuentas-premium.80/page-3',
            'https://forowarez.net/forums/cuentas-premium.80/page-4',
            'https://forowarez.net/forums/cuentas-premium.80/page-5',
            'https://forowarez.net/forums/cuentas-premium.80/page-6',
            'https://forowarez.net/forums/cuentas-premium.80/page-7',
            'https://forowarez.net/forums/cuentas-premium.80/page-8',
            'https://forowarez.net/forums/cuentas-premium.80/page-9',
            'https://forowarez.net/forums/cuentas-premium.80/page-10',
            'https://forowarez.net/forums/cuentas-premium.80/page-11',
            'https://forowarez.net/forums/cuentas-premium.80/page-12',
            'https://forowarez.net/forums/cuentas-premium.80/page-13',
            'https://forowarez.net/forums/cuentas-premium.80/page-14',
            'https://forowarez.net/forums/cuentas-premium.80/page-15',
            'https://forowarez.net/forums/cuentas-premium.80/page-16',
            'https://forowarez.net/forums/cuentas-premium.80/page-17',
            'https://forowarez.net/forums/cuentas-premium.80/page-18',
            'https://forowarez.net/forums/cuentas-premium.80/page-19',
            'https://forowarez.net/forums/cuentas-premium.80/page-20',
            'https://forowarez.net/forums/cuentas-premium.80/page-21',
            'https://forowarez.net/forums/cuentas-premium.80/page-22',
            'https://forowarez.net/forums/cuentas-premium.80/page-23',
        ]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        lista_tipo_cuentas = response.css(
            '.structItem-cell.structItem-cell--main > .structItem-title > .labelLink > span::text').extract()
        lista_nombre_oferta = response.css(
            '.structItem-cell.structItem-cell--main > .structItem-title > a::text').extract()
        lista_fecha = response.css(
            '.structItem-cell.structItem-cell--main > .structItem-minor > ul > .structItem-startDate > a > time::attr(datetime)').extract()
        lista_usuarios = response.css(
            '.structItem-cell.structItem-cell--main > .structItem-minor > ul > li > a::text').extract()
        lista_visitas = response.css(
            '.structItem-cell.structItem-cell--meta > .pairs.pairs--justified.structItem-minor > dd::text ').extract()
        with open(nombre_archivo, 'a+') as f:
            for index in range(len(lista_tipo_cuentas)):
                lista_fecha
                f.write(lista_tipo_cuentas[index] + "," + lista_nombre_oferta[index].replace(',', ' ') + "," +
                        modifyDates.get_date(lista_fecha[index]).split('-')[0] + "," +
                        modifyDates.get_date(lista_fecha[index]).split('-')[1] + "," +
                        modifyDates.get_date(lista_fecha[index]).split('-')[2] + "," +
                        modifyDates.get_hour(lista_fecha[index]).split(':')[0] + "," + lista_usuarios[index].replace(
                    ',', ' ') + ',' + lista_visitas[index] + '\n')


class modifyDates:
    def get_date(fecha):
        return fecha.split('T')[0]

    def get_hour(fecha):
        return fecha.split('T')[1]