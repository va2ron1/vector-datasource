# -*- encoding: utf-8 -*-
from shapely.wkt import loads as wkt_loads
import dsl
from . import FixtureTest


class FunicularMonorail(FixtureTest):
    def test_monorail(self):
        self.generate_fixtures(dsl.way(1087040962, wkt_loads('POINT (-122.400593309427 37.6308797229248)'), {u'source': u'openstreetmap.org', u'railway': u'buffer_stop'}),dsl.way(1087054505, wkt_loads('POINT (-122.400544261413 37.63086456945589)'), {u'source': u'openstreetmap.org', u'railway': u'buffer_stop'}),dsl.way(38852089, wkt_loads('LINESTRING (-122.400593309427 37.6308797229248, -122.401218986023 37.62993209160209, -122.401309805698 37.62978126628298, -122.401369004675 37.62963876453279, -122.401417603532 37.62946026345269, -122.401440780066 37.629287666943, -122.401434581691 37.62913840549959, -122.401378167491 37.62878780356129)'), {u'bridge': u'yes', u'layer': u'5', u'name': u'AirTrain Blue Line', u'source': u'openstreetmap.org', u'railway': u'monorail'}),dsl.way(38852167, wkt_loads('LINESTRING (-122.395028785231 37.61484121342899, -122.395016837638 37.614339260453, -122.39501459185 37.61392319337519, -122.395013513871 37.6137637964434, -122.394998242512 37.6137026704758, -122.394970304906 37.61362048123168, -122.394933923137 37.6135348050746, -122.394893498949 37.61347816197959, -122.394841217 37.61341810317349, -122.394773573859 37.6133614599896, -122.394676196482 37.61330410516398, -122.394568757974 37.6132579224, -122.394496533425 37.61323522238688, -122.39439691026 37.61321629384399, -122.394297646421 37.6132067584108, -122.394186524821 37.61321138380771, -122.39408771014 37.61323045467168)'), {u'bridge': u'yes', u'layer': u'5', u'name': u'AirTrain Blue Line', u'source': u'openstreetmap.org', u'oneway': u'yes', u'railway': u'monorail'}),dsl.way(93670218, wkt_loads('LINESTRING (-122.39408771014 37.61323045467168, -122.390710763324 37.6140636616382, -122.387362382933 37.6148763656653, -122.387250812175 37.61490141340239, -122.387122712416 37.61492489564829, -122.387006380586 37.6149439660729, -122.386880526615 37.61495869583779, -122.386401994063 37.61499505770859, -122.386292040272 37.6150041659631, -122.386175977938 37.6150157647544, -122.386077522583 37.61503711221809, -122.385321141113 37.615216786462, -122.385232028237 37.61523927239621, -122.38513698648 37.6152720762311, -122.385051916023 37.61531925395519, -122.384969181185 37.61538379417189, -122.384916719572 37.6154521056963, -122.384446092195 37.61615898397348, -122.384405937502 37.6162377548733, -122.384390127153 37.6163090542066, -122.384390935637 37.61639095585141, -122.384408632448 37.61645129688389, -122.384656118309 37.61707220895609, -122.384694476371 37.61714528639389, -122.3847561008 37.61720690762449, -122.384817545565 37.61725045516079, -122.384901178718 37.61728759862749, -122.385777215783 37.61765625720198, -122.385878635579 37.61768678298921, -122.385976102787 37.6177027218569, -122.386078690392 37.61770179683341, -122.386178583052 37.6176880637912, -122.387059021862 37.61747295990338, -122.387192062356 37.61743617230879, -122.387330133415 37.61738885361589, -122.387453561935 37.61734395419668, -122.388091904776 37.6170998887341, -122.388243989553 37.61704210985419, -122.388413591479 37.61698988112369, -122.388573222105 37.61694761424948, -122.39052014082 37.61646965534869, -122.390918992806 37.61637266852409, -122.391022119401 37.6163674740685, -122.391131713866 37.6163523887979, -122.391239960857 37.61634107484299, -122.391420342566 37.61632769733439, -122.391538740521 37.61631090428819, -122.391646358692 37.6162887033061, -122.391757480293 37.6162635848792, -122.393933110079 37.61573389007109)'), {u'bridge': u'yes', u'layer': u'5', u'name': u'AirTrain Blue Line', u'source': u'openstreetmap.org', u'oneway': u'yes', u'railway': u'monorail'}),dsl.way(93671417, wkt_loads('LINESTRING (-122.393933110079 37.61573389007109, -122.394066779393 37.6157013710702, -122.394206018262 37.6156705598374, -122.39433223156 37.6156594592516, -122.39447919594 37.6156563994744, -122.395759834209 37.6156487144522, -122.396523312369 37.61564302184259, -122.3967407945 37.6156441603646, -122.396860090769 37.61566778469109, -122.396959893597 37.6156966035131, -122.397042628435 37.6157301898791, -122.397122488664 37.61577822120248, -122.397190131805 37.61582475818847, -122.397248522298 37.61588047444989, -122.397313380662 37.61595248569899, -122.397350031925 37.61601076352649, -122.397378778014 37.6160635622026, -122.397438246486 37.61621761742448, -122.398603271578 37.61943121484968, -122.398895134214 37.6201089535842, -122.398976072421 37.62030661732379, -122.399278445346 37.62120271481319, -122.399588813276 37.6220983745929, -122.399651964841 37.62226408612259, -122.399754372783 37.62258889103349, -122.39981411075 37.622810099086, -122.399848606057 37.62296435378089, -122.399995929763 37.6234848898632, -122.400355884698 37.62453327945192, -122.400688980005 37.62552345507729, -122.400746831509 37.6256812615427)'), {u'bridge': u'yes', u'layer': u'5', u'name': u'AirTrain Blue Line', u'source': u'openstreetmap.org', u'oneway': u'yes', u'railway': u'monorail'}),dsl.way(286832376, wkt_loads('LINESTRING (-122.400746831509 37.6256812615427, -122.400892178922 37.6261316982625, -122.400962696672 37.62639807434009, -122.401029621161 37.62691851523068, -122.401077321702 37.62733806690879, -122.401072291137 37.6276058615865, -122.401090257442 37.62784982141349, -122.401214045288 37.62857571988958, -122.401311961654 37.62917227037191, -122.401342504374 37.62942298377889, -122.401318968514 37.62959750086969, -122.401264889934 37.62975622355889, -122.401161763339 37.62992191801709, -122.400544261413 37.63086456945589)'), {u'bridge': u'yes', u'layer': u'5', u'name': u'AirTrain Blue Line', u'source': u'openstreetmap.org', u'oneway': u'yes', u'railway': u'monorail'}),dsl.way(427295091, wkt_loads('LINESTRING (-122.401378167491 37.62878780356129, -122.401181346612 37.62755549007899, -122.401078759007 37.6269094084358, -122.401023243122 37.62644339517491, -122.40095083891 37.62610238545209, -122.400869271882 37.62583835619438, -122.400722127839 37.62542342068819, -122.40049413542 37.62472559525839, -122.400105883554 37.62358770171189, -122.399942300341 37.62301579565828, -122.399887233614 37.62279658043968, -122.399822105756 37.6225713878916, -122.399642802025 37.62207695800501, -122.399352107199 37.62118570941109, -122.399030240833 37.62029736741248, -122.39894543987 37.6200992055748, -122.398658697631 37.6194187628991, -122.397468340048 37.61615948207339, -122.397445882166 37.61609906964689, -122.397411207196 37.61600642293288, -122.397355421817 37.615909222032, -122.39729918728 37.61584098208498, -122.397235137401 37.61577651342269, -122.39716749426 37.61572727242, -122.397064188002 37.6156682827943, -122.396965013995 37.6156299999965, -122.396854521215 37.61560239082898, -122.396717528134 37.61558460141158, -122.396281665558 37.61558068773908, -122.396075592032 37.61558317825799, -122.39581391279 37.6155821820505, -122.39568464522 37.6155779837472, -122.395555197988 37.61557335849749, -122.395445783186 37.61555208234538, -122.395340410803 37.61550917423418, -122.395242404606 37.6154528884321, -122.39516389185 37.61538215754079, -122.395102357253 37.61531349016249, -122.395059687277 37.61523436249339, -122.395034085291 37.61512356938368, -122.395026629275 37.61502380563309, -122.395028785231 37.61484121342899)'), {u'bridge': u'yes', u'layer': u'5', u'name': u'AirTrain Blue Line', u'bridge:structure': u'beam', u'source': u'openstreetmap.org', u'oneway': u'yes', u'railway': u'monorail'}),dsl.way(-6043603, wkt_loads('LINESTRING (-122.400593309427 37.6308797229248, -122.401218986023 37.62993209160209, -122.401309805698 37.62978126628298, -122.401369004675 37.62963876453279, -122.401417603532 37.62946026345269, -122.401440780066 37.629287666943, -122.401434581691 37.62913840549959, -122.401378167491 37.62878780356129, -122.401181346612 37.62755549007899, -122.401078759007 37.6269094084358, -122.401023243122 37.62644339517491, -122.40095083891 37.62610238545209, -122.400869271882 37.62583835619438, -122.400722127839 37.62542342068819, -122.40049413542 37.62472559525839, -122.400105883554 37.62358770171189, -122.399942300341 37.62301579565828, -122.399887233614 37.62279658043968, -122.399822105756 37.6225713878916, -122.399642802025 37.62207695800501, -122.399352107199 37.62118570941109, -122.399030240833 37.62029736741248, -122.39894543987 37.6200992055748, -122.398658697631 37.6194187628991, -122.397468340048 37.61615948207339, -122.397445882166 37.61609906964689, -122.397411207196 37.61600642293288, -122.397355421817 37.615909222032, -122.39729918728 37.61584098208498, -122.397235137401 37.61577651342269, -122.39716749426 37.61572727242, -122.397064188002 37.6156682827943, -122.396965013995 37.6156299999965, -122.396854521215 37.61560239082898, -122.396717528134 37.61558460141158, -122.396281665558 37.61558068773908, -122.396075592032 37.61558317825799, -122.39581391279 37.6155821820505, -122.39568464522 37.6155779837472, -122.395555197988 37.61557335849749, -122.395445783186 37.61555208234538, -122.395340410803 37.61550917423418, -122.395242404606 37.6154528884321, -122.39516389185 37.61538215754079, -122.395102357253 37.61531349016249, -122.395059687277 37.61523436249339, -122.395034085291 37.61512356938368, -122.395026629275 37.61502380563309, -122.395028785231 37.61484121342899, -122.395016837638 37.614339260453, -122.39501459185 37.61392319337519, -122.395013513871 37.6137637964434, -122.394998242512 37.6137026704758, -122.394970304906 37.61362048123168, -122.394933923137 37.6135348050746, -122.394893498949 37.61347816197959, -122.394841217 37.61341810317349, -122.394773573859 37.6133614599896, -122.394676196482 37.61330410516398, -122.394568757974 37.6132579224, -122.394496533425 37.61323522238688, -122.39439691026 37.61321629384399, -122.394297646421 37.6132067584108, -122.394186524821 37.61321138380771, -122.39408771014 37.61323045467168, -122.390710763324 37.6140636616382, -122.387362382933 37.6148763656653, -122.387250812175 37.61490141340239, -122.387122712416 37.61492489564829, -122.387006380586 37.6149439660729, -122.386880526615 37.61495869583779, -122.386401994063 37.61499505770859, -122.386292040272 37.6150041659631, -122.386175977938 37.6150157647544, -122.386077522583 37.61503711221809, -122.385321141113 37.615216786462, -122.385232028237 37.61523927239621, -122.38513698648 37.6152720762311, -122.385051916023 37.61531925395519, -122.384969181185 37.61538379417189, -122.384916719572 37.6154521056963, -122.384446092195 37.61615898397348, -122.384405937502 37.6162377548733, -122.384390127153 37.6163090542066, -122.384390935637 37.61639095585141, -122.384408632448 37.61645129688389, -122.384656118309 37.61707220895609, -122.384694476371 37.61714528639389, -122.3847561008 37.61720690762449, -122.384817545565 37.61725045516079, -122.384901178718 37.61728759862749, -122.385777215783 37.61765625720198, -122.385878635579 37.61768678298921, -122.385976102787 37.6177027218569, -122.386078690392 37.61770179683341, -122.386178583052 37.6176880637912, -122.387059021862 37.61747295990338, -122.387192062356 37.61743617230879, -122.387330133415 37.61738885361589, -122.387453561935 37.61734395419668, -122.388091904776 37.6170998887341, -122.388243989553 37.61704210985419, -122.388413591479 37.61698988112369, -122.388573222105 37.61694761424948, -122.39052014082 37.61646965534869, -122.390918992806 37.61637266852409, -122.391022119401 37.6163674740685, -122.391131713866 37.6163523887979, -122.391239960857 37.61634107484299, -122.391420342566 37.61632769733439, -122.391538740521 37.61631090428819, -122.391646358692 37.6162887033061, -122.391757480293 37.6162635848792, -122.393933110079 37.61573389007109, -122.394066779393 37.6157013710702, -122.394206018262 37.6156705598374, -122.39433223156 37.6156594592516, -122.39447919594 37.6156563994744, -122.395759834209 37.6156487144522, -122.396523312369 37.61564302184259, -122.3967407945 37.6156441603646, -122.396860090769 37.61566778469109, -122.396959893597 37.6156966035131, -122.397042628435 37.6157301898791, -122.397122488664 37.61577822120248, -122.397190131805 37.61582475818847, -122.397248522298 37.61588047444989, -122.397313380662 37.61595248569899, -122.397350031925 37.61601076352649, -122.397378778014 37.6160635622026, -122.397438246486 37.61621761742448, -122.398603271578 37.61943121484968, -122.398895134214 37.6201089535842, -122.398976072421 37.62030661732379, -122.399278445346 37.62120271481319, -122.399588813276 37.6220983745929, -122.399651964841 37.62226408612259, -122.399754372783 37.62258889103349, -122.39981411075 37.622810099086, -122.399848606057 37.62296435378089, -122.399995929763 37.6234848898632, -122.400355884698 37.62453327945192, -122.400688980005 37.62552345507729, -122.400746831509 37.6256812615427, -122.400892178922 37.6261316982625, -122.400962696672 37.62639807434009, -122.401029621161 37.62691851523068, -122.401077321702 37.62733806690879, -122.401072291137 37.6276058615865, -122.401090257442 37.62784982141349, -122.401214045288 37.62857571988958, -122.401311961654 37.62917227037191, -122.401342504374 37.62942298377889, -122.401318968514 37.62959750086969, -122.401264889934 37.62975622355889, -122.401161763339 37.62992191801709, -122.400544261413 37.63086456945589)'), {u'name': u'AirTrain Blue Line', u'source': u'openstreetmap.org', u'colour': u'blue', u'route_name': u'AirTrain Blue Line', u'route_pref_color': u'0', u'ref': u'BLUE', u'route': u'monorail'}))  # noqa

        self.assert_has_feature(
            16, 10486, 25367, 'transit',
            {'kind': 'monorail'})

    def test_funicular(self):
        self.generate_fixtures(dsl.way(54834749, wkt_loads('LINESTRING (-80.01764782181549 40.439810883179, -80.0187104389651 40.43836799398048)'), {u'website': u'http://www.duquesneincline.org', u'name': u'Dusquesne Incline', u'wikipedia': u'en:Duquesne Incline', u'source': u'openstreetmap.org', u'historic': u'yes', u'gauge': u'1524', u'heritage': u'2', u'wikidata': u'Q1266663', u'railway': u'funicular', u'ref:nrhp': u'75001609', u'heritage:operator': u'nrhp', u'incline': u'up'}),dsl.way(-6060405, wkt_loads('LINESTRING (-80.01764782181549 40.439810883179, -80.0187104389651 40.43836799398048)'), {u'route_pref_color': u'0', u'source': u'openstreetmap.org', u'route': u'funicular', u'route_name': u'Dusquesne Incline', u'name': u'Dusquesne Incline'}))  # noqa

        self.assert_has_feature(
            16, 18201, 24705, 'transit',
            {'kind': 'funicular'})
