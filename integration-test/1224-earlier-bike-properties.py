# -*- encoding: utf-8 -*-
from shapely.wkt import loads as wkt_loads
import dsl
from . import FixtureTest


class EarlierBikeProperties(FixtureTest):
    def test_bobcat_trail(self):
        self.generate_fixtures(dsl.way(12188550, wkt_loads('LINESTRING (-122.503567010783 37.85385707362148, -122.503669957714 37.85361988650629, -122.503842973238 37.8533814928264, -122.503998381782 37.8532565149332, -122.504238591289 37.8531784213748, -122.504535394659 37.85314941112169, -122.504744522457 37.85311820203478, -122.504863189906 37.85308245342809, -122.504990301519 37.85303790950498, -122.505083636477 37.85298208770357, -122.505159903445 37.8528927869193, -122.505202303926 37.8527544733385, -122.505210837921 37.85264290019418, -122.505210837921 37.85257147343288, -122.505151369449 37.852513523368, -122.504990301519 37.85245990001168, -122.504682808197 37.85233896359521, -122.504133398569 37.85183748320019, -122.504150646223 37.85162738530789, -122.504339382264 37.85143090564348, -122.504648402722 37.8513223805502, -122.504940265358 37.85113270951338, -122.505111933408 37.85095651503899, -122.505180564696 37.85076670119689, -122.50521488034 37.85058369635739, -122.505137715057 37.85033968919799, -122.505060370111 37.8499194842786, -122.50467418437 37.84909268651379, -122.504545365959 37.84894358387118, -122.504408103383 37.8488215776786, -122.504383938702 37.84872702274049, -122.504400377872 37.84866658696258, -122.50444843774 37.84864608702188, -122.504498294238 37.8486272185595, -122.504710206813 37.84864140537379, -122.504889959702 37.84865722366861, -122.505111933408 37.84861828086499, -122.505438111688 37.84850308381748, -122.505815673602 37.84846236757661, -122.505970183831 37.84842846100348, -122.50603890495 37.84832681212479, -122.506047528777 37.84819806613529, -122.506099002243 37.8480015063977, -122.50616763353 37.84775749069299, -122.506283875528 37.8476269703335, -122.506390775047 37.84762200488039, -122.506476564156 37.8476625797153, -122.506562532929 37.84771691591028, -122.506656945866 37.84782530444078, -122.506759892797 37.84784559180508, -122.506871373724 37.84779820732308, -122.506914403026 37.84766938947558, -122.506845681907 37.84747289926387, -122.506759892797 37.8471881648655, -122.506828524085 37.8469645050118, -122.506914403026 37.846795110418, -122.507103228899 37.8466528129836, -122.50757529358 37.84644936831839, -122.507815592919 37.84634778764779, -122.507995794965 37.84621215737228, -122.508227560308 37.84611731534209, -122.508510799117 37.8461376741128, -122.508682467168 37.84609695656579, -122.508759722283 37.8459817555793, -122.508888540694 37.84566317851537, -122.508888540694 37.84541915507289, -122.508759722283 37.84512781556228, -122.508450701825 37.84486336029369, -122.508021576614 37.8445583984941, -122.507806969092 37.84440261849789, -122.507626767046 37.84435508992708, -122.507412159525 37.84432799153431, -122.507257739128 37.8443211814654, -122.50720617583 37.8442533644951, -122.507197641835 37.84415178079959, -122.507618233051 37.8438400059441, -122.508425010008 37.84345360192218, -122.509188937325 37.84317566217979, -122.509577907843 37.84308067436561, -122.510081503392 37.84289757951078, -122.510545034078 37.84267419040318, -122.511085730048 37.84232168966969, -122.511420532154 37.84221329305, -122.511849567534 37.8420912757219, -122.512175835645 37.84200990707758, -122.512690839797 37.8420505559408, -122.513008304419 37.84198961810781, -122.513257227584 37.84188107911888, -122.513583405864 37.84165747410998, -122.513995373253 37.84111520077172, -122.514081162363 37.8409592716196, -122.514252920245 37.84015947332518, -122.514381558994 37.8399155026141, -122.514604790342 37.8397663104732, -122.514965194434 37.83973835908269, -122.515201002196 37.8396911112768, -122.515352817479 37.83962158742329, -122.515463489922 37.83954936767749, -122.515628600271 37.83941649167359, -122.515748525362 37.8392365801625, -122.51594417843 37.8387631043173, -122.516360008575 37.83774675977749, -122.517188704425 37.83622796333779, -122.517773687338 37.8355327601591, -122.517856242513 37.83544485717809)'), {u'horse': u'yes', u'tiger:name_base': u'Bobcat', u'bicycle': u'yes', u'name': u'Bobcat Trail', u'tiger:cfcc': u'A41', u'tiger:reviewed': u'no', u'surface': u'dirt', u'access': u'yes', u'source': u'openstreetmap.org', u'tiger:county': u'Marin, CA', u'tiger:name_type': u'Trl', u'motor_vehicle': u'no', u'foot': u'yes', u'sidewalk': u'none', u'tracktype': u'grade2', u'highway': u'track'}))  # noqa

        self.assert_has_feature(
            13, 1308, 3164, 'roads',
            {'motor_vehicle': 'no'})
