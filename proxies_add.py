import random

mode_proxy = "socks5"
host_proxy = 'rp.proxyscrape.com'
port_proxy = 6060
password_proxy = "83hl64r1qc4k6eg"


proxies_username = [
    "ycuvm8oc8xfyfyv-country-us-session-v96qgugvis-lifetime-10",
    "ycuvm8oc8xfyfyv-country-us-session-n4qo8b9xu4-lifetime-10",
    "ycuvm8oc8xfyfyv-country-us-session-uvmos77aha-lifetime-10",
    "ycuvm8oc8xfyfyv-country-us-session-ry9skxqefv-lifetime-10",
    "ycuvm8oc8xfyfyv-country-us-session-gtfstjzqy2-lifetime-10",
    "ycuvm8oc8xfyfyv-country-us-session-23xci5dr94-lifetime-10",
    "ycuvm8oc8xfyfyv-country-us-session-fbhk8g5gn4-lifetime-10",
    "ycuvm8oc8xfyfyv-country-us-session-aqv98cg790-lifetime-10",
    "ycuvm8oc8xfyfyv-country-us-session-vg81fa9js9-lifetime-10",
    "ycuvm8oc8xfyfyv-country-us-session-h9ph2acnuc-lifetime-10",
    "ycuvm8oc8xfyfyv-country-us-session-kd4rp7tpg0-lifetime-10",
    "ycuvm8oc8xfyfyv-country-us-session-pge29705ra-lifetime-10",
    "ycuvm8oc8xfyfyv-country-us-session-2n9aekoff2-lifetime-10",
    "ycuvm8oc8xfyfyv-country-us-session-awyu4hm87d-lifetime-10",
    "ycuvm8oc8xfyfyv-country-us-session-7j5p8lsyba-lifetime-10",
    "ycuvm8oc8xfyfyv-country-us-session-y3p1z8i4jw-lifetime-10",
    "ycuvm8oc8xfyfyv-country-us-session-w9d1jxxkbi-lifetime-10",
    "ycuvm8oc8xfyfyv-country-us-session-thbgxsyztf-lifetime-10",
    "ycuvm8oc8xfyfyv-country-us-session-2juiks0bmm-lifetime-10",
    "ycuvm8oc8xfyfyv-country-us-session-qla23kube8-lifetime-10",
    "ycuvm8oc8xfyfyv-country-us-session-ilawye9oas-lifetime-10",
    "ycuvm8oc8xfyfyv-country-us-session-3xlollq1ow-lifetime-10",
    "ycuvm8oc8xfyfyv-country-us-session-zgo5jr4bma-lifetime-10",
    "ycuvm8oc8xfyfyv-country-us-session-ad8j3hk1lq-lifetime-10",
    "ycuvm8oc8xfyfyv-country-us-session-n6br7zindx-lifetime-10",
    "ycuvm8oc8xfyfyv-country-us-session-a5zr35qa5a-lifetime-10",
    "ycuvm8oc8xfyfyv-country-us-session-h7h7kehxsb-lifetime-10",
    "ycuvm8oc8xfyfyv-country-us-session-7vvse7zpoe-lifetime-10",
    "ycuvm8oc8xfyfyv-country-us-session-ak2m40h840-lifetime-10",
    "ycuvm8oc8xfyfyv-country-us-session-28bsdvr7s2-lifetime-10",
    "ycuvm8oc8xfyfyv-country-us-session-x2dwwxuknw-lifetime-10",
    "ycuvm8oc8xfyfyv-country-us-session-c9cc1srlmu-lifetime-10",
    "ycuvm8oc8xfyfyv-country-us-session-awqgdm58zz-lifetime-10",
    "ycuvm8oc8xfyfyv-country-us-session-p4gf0ns9f1-lifetime-10",
    "ycuvm8oc8xfyfyv-country-us-session-vvm4yd0ger-lifetime-10",
    "ycuvm8oc8xfyfyv-country-us-session-mi9mbhcg4i-lifetime-10",
    "ycuvm8oc8xfyfyv-country-us-session-8noucif7od-lifetime-10",
    "ycuvm8oc8xfyfyv-country-us-session-kledhumgeo-lifetime-10",
    "ycuvm8oc8xfyfyv-country-us-session-xpux4lvbt5-lifetime-10",
    "ycuvm8oc8xfyfyv-country-us-session-tqc40e8jaw-lifetime-10",
    "ycuvm8oc8xfyfyv-country-us-session-xcs9nm8ci2-lifetime-10",
    "ycuvm8oc8xfyfyv-country-us-session-1yj0s687bm-lifetime-10",
    "ycuvm8oc8xfyfyv-country-us-session-nz4szotky7-lifetime-10",
    "ycuvm8oc8xfyfyv-country-us-session-kivhnjk7ya-lifetime-10",
    "ycuvm8oc8xfyfyv-country-us-session-j2l6ubshkr-lifetime-10",
    "ycuvm8oc8xfyfyv-country-us-session-8dqjrgg7np-lifetime-10",
    "ycuvm8oc8xfyfyv-country-us-session-gj5y8pw459-lifetime-10",
    "ycuvm8oc8xfyfyv-country-us-session-bazq4ei8mq-lifetime-10",
    "ycuvm8oc8xfyfyv-country-us-session-19ik4belim-lifetime-10",
    "ycuvm8oc8xfyfyv-country-us-session-aei1aoeqm5-lifetime-10",
    "ycuvm8oc8xfyfyv-country-us-session-jrnt5wxtcn-lifetime-10",
    "ycuvm8oc8xfyfyv-country-us-session-i8t43iz4zd-lifetime-10",
    "ycuvm8oc8xfyfyv-country-us-session-zxq7age19k-lifetime-10",
    "ycuvm8oc8xfyfyv-country-us-session-qxpph10nf9-lifetime-10",
    "ycuvm8oc8xfyfyv-country-us-session-kdqbh0p5ie-lifetime-10",
    "ycuvm8oc8xfyfyv-country-us-session-wg76s3fvgr-lifetime-10",
    "ycuvm8oc8xfyfyv-country-us-session-uk0ohzfwaf-lifetime-10",
    "ycuvm8oc8xfyfyv-country-us-session-lwn8hq62on-lifetime-10",
    "ycuvm8oc8xfyfyv-country-us-session-4u3byrdjsg-lifetime-10",
    "ycuvm8oc8xfyfyv-country-us-session-7co6beacos-lifetime-10",
    "ycuvm8oc8xfyfyv-country-us-session-rugqrh1n8g-lifetime-10",
    "ycuvm8oc8xfyfyv-country-us-session-7yb27w6brw-lifetime-10",
    "ycuvm8oc8xfyfyv-country-us-session-4vct4cdout-lifetime-10",
    "ycuvm8oc8xfyfyv-country-us-session-mhk8syl9go-lifetime-10",
    "ycuvm8oc8xfyfyv-country-us-session-v2a3zdg03j-lifetime-10",
    "ycuvm8oc8xfyfyv-country-us-session-jf347hu1zm-lifetime-10",
    "ycuvm8oc8xfyfyv-country-us-session-v2fok8wm0x-lifetime-10",
    "ycuvm8oc8xfyfyv-country-us-session-wa7ou48x7h-lifetime-10",
    "ycuvm8oc8xfyfyv-country-us-session-9wh5bpzxgp-lifetime-10",
    "ycuvm8oc8xfyfyv-country-us-session-tjw18cknb1-lifetime-10",
    "ycuvm8oc8xfyfyv-country-us-session-g7fuyadgcm-lifetime-10",
    "ycuvm8oc8xfyfyv-country-us-session-u9rsgei3da-lifetime-10",
    "ycuvm8oc8xfyfyv-country-us-session-h01b697tvl-lifetime-10",
    "ycuvm8oc8xfyfyv-country-us-session-a8kloqacpe-lifetime-10",
    "ycuvm8oc8xfyfyv-country-us-session-9by86cegok-lifetime-10",
    "ycuvm8oc8xfyfyv-country-us-session-9oslk42pmg-lifetime-10",
    "ycuvm8oc8xfyfyv-country-us-session-3jofzwq91b-lifetime-10",
    "ycuvm8oc8xfyfyv-country-us-session-45q51efoyn-lifetime-10",
    "ycuvm8oc8xfyfyv-country-us-session-sjiwuk5evh-lifetime-10",
    "ycuvm8oc8xfyfyv-country-us-session-z50sgr71jp-lifetime-10",
    "ycuvm8oc8xfyfyv-country-us-session-d3m1zaeh3i-lifetime-10",
    "ycuvm8oc8xfyfyv-country-us-session-p4eu1doder-lifetime-10",
    "ycuvm8oc8xfyfyv-country-us-session-mx491xs3c8-lifetime-10",
    "ycuvm8oc8xfyfyv-country-us-session-vvrcbowxxd-lifetime-10",
    "ycuvm8oc8xfyfyv-country-us-session-42bobv472n-lifetime-10",
    "ycuvm8oc8xfyfyv-country-us-session-fr2qqijeqj-lifetime-10",
    "ycuvm8oc8xfyfyv-country-us-session-sj0l0t0o6o-lifetime-10",
    "ycuvm8oc8xfyfyv-country-us-session-sm8lx17861-lifetime-10",
    "ycuvm8oc8xfyfyv-country-us-session-j3l3eknzay-lifetime-10",
    "ycuvm8oc8xfyfyv-country-us-session-zu62w85q8h-lifetime-10",
    "ycuvm8oc8xfyfyv-country-us-session-6y0ok9og7l-lifetime-10",
    "ycuvm8oc8xfyfyv-country-us-session-sc5fc2ut68-lifetime-10",
    "ycuvm8oc8xfyfyv-country-us-session-117bnkbicf-lifetime-10",
    "ycuvm8oc8xfyfyv-country-us-session-77i9ssupqq-lifetime-10",
    "ycuvm8oc8xfyfyv-country-us-session-77cgd2l60p-lifetime-10",
    "ycuvm8oc8xfyfyv-country-us-session-c4mulqn2qq-lifetime-10",
    "ycuvm8oc8xfyfyv-country-us-session-9ffbe9item-lifetime-10",
    "ycuvm8oc8xfyfyv-country-us-session-wb47msvlou-lifetime-10",
    "ycuvm8oc8xfyfyv-country-us-session-ewkv4s4pak-lifetime-10",
    "ycuvm8oc8xfyfyv-country-us-session-ecdw3vm1ka-lifetime-10",
    "ycuvm8oc8xfyfyv-country-us-session-jdb5l9tt5f-lifetime-10",
]

username_proxy = random.choice(proxies_username)