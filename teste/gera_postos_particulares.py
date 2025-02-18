from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

lista_links = [
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/a-mais-medicina-diagnostica-unid-hospital-ibcc-2-5",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/afip-cdb-hospital-leforte-2-26",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/afip-hospital-tiradentes-2-27",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/agencia-tranfusional-hospital-alvorada-moema-2-29",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/agencia-transfusional-do-hospital-e-maternidade-sacre-coeur-2-32",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/agencia-transfusional-do-hospital-nossa-senhora-do-rosario-2-35",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/agencia-transfusional-do-hospital-sabara-2-42",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/agencia-transfusional-do-hospital-santa-cecilia-2-43",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/agencia-transfusional-do-hospital-sao-luiz-analia-franco-2-47",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/agencia-transfusional-do-hospital-total-cor-2-49",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/agencia-transfusional-hospital-do-coracao-2-57",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/agencia-transfusional-hospital-edmundo-vasconcelos-2-58",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/agencia-transfusional-hospital-metropolitano-2-61",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/agencia-transfusional-hospital-nipo-brasileiro-2-64",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/agencia-transfusional-hospital-paulistano-2-67",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/agencia-transfusional-hospital-pro-matre-paulista-2-69",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/agencia-transfusional-hospital-samaritano-paulista-2-73",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/agencia-transfusional-hospital-santa-joana-2-75",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/agencia-transfusional-hospital-sao-cristovao-2-77",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/agencia-transfusional-hospital-sao-luiz-analia-franco-2-79",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/agencia-transfusional-hospital-sao-luiz-jabaquara-2-80",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/agencia-transfusional-hospital-sao-luiz-morumbi-2-81",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/agencia-transfusional-hospital-vila-nova-star-2-83",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/albert-einstein-unidade-chacara-klabin-2-98",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/alta-excelencia-diagnostica-hospital-sabara-2-111",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/alvorada-moema-centro-medico-ortopedico-2-112",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/amb-descentralizado-lapa-hspm-2-123",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/amb-descentralizado-santo-amaro-hspm-2-124",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/amb-descentralizado-tucuruvi-hspm-2-125",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/amb-descentralizado-v-carrao-hspm-2-126",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/ambulatorio-programa-einstein-comunidade-paraisopolis-2-142",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/ambulatorio-vitoria-analia-franco-2-145",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/ambulatorios-de-filantropia-do-hospital-sirio-libanes-2-147",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/americas-servico-e-saude-2-151",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/analia-franco-day-hospital-de-cirurgia-plastica-2-156",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/associacao-hospital-personal-cuidados-especiais-2-197",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/banco-de-sangue-do-hospital-cruz-azul-de-sao-paulo-2-238",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/bella-servicos-de-cirurgia-plastica-2-247",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/bla-servicos-hospitalares-2-269",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/bv-sede-2-278",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/cdb-centro-de-diagnosticos-brasil-2-321",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/cdb-centro-de-diagnosticos-brasil-2-322",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/cdb-centro-de-diagnosticos-brasil-2-324",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/cdb-centro-de-diagnosticos-brasil-ana-rosa-2-326",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/cdb-centro-de-diagnosticos-brasil-mooca-2-327",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/cdb-moema-2-328",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/cdb-penha-2-330",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/cdb-perdizes-2-331",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/cdb-premium-2-332",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/cdb-tatuape-2-336",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/cdb-tks-marselhesa-500-2-337",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/cdb-tks-santana-2-338",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/cema-clinica-oftalmo-e-otorrino-aricanduva-2-343",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/cema-hosp-espec-2-344",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/cema-hospital-especializado-eldorado-2-346",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/cema-hospital-especializado-ibirapuera-2-347",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/cema-hospital-especializado-itaquera-2-348",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/cema-hospital-especializado-ltda-tucuruvi-2-350",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/cema-hospital-especializado-morumbi-2-351",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/cema-hospital-especializado-patio-paulista-2-352",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/cema-hospital-especializado-santana-2-353",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/cema-hospital-especializado-vila-olimpia-2-355",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/cema-hospital-especializado-west-plaza-2-356",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/cema-interlagos-2-357",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/centro-de-atendimento-hospitalar-a-mulher-presa-2-373",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/centro-de-medicina-especializada-santa-paula-2-377",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/centro-medico-aviccena-2-411",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/centro-medico-especializado-nove-de-julho-2-418",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/centro-medico-hospital-sao-luiz-itaim-2-423",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/centro-medico-samaritano-higienopolis-2-439",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/certa-centro-de-referencia-em-tratamentos-avancados-hospital-2-455",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/cesmo-eye-hospital-analia-franco-2-456",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/cetene-hospital-9-de-julho-2-458",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/cientificalab-hospital-campo-limpo-2-474",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/cientificalab-hospital-sao-cristovao-2-475",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/cirucard-2-484",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/clinica-de-retaguarda-hospitalar-moema-2-543",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/clinica-einstein-analia-franco-2-561",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/clinica-einstein-on-site-2-562",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/clinica-einstein-santana-2-563",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/clinica-espec-ciama-2-566",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/clinica-espec-ophthal-2-567",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/clinicas-de-especialidades-vidas-campo-limpo-2-636",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/clinicas-de-especialidades-vital-tatuape-2-637",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/cma-servicos-medicos-hospitalares-ltda-2-653",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/complexo-hospitalar-paulista-2-697",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/complexo-hospitalar-santo-expedito-2-699",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/cons-medico-goncalves-assist-medica-e-hospitalar-2-713",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/cons-medico-houmsi-2-714",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/cons-medico-pediatrics-home-care-2-715",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/cons-medico-rhem-2-716",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/cons-medico-wr-assevera-2-717",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/cuidar-e-saude-2-742",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/day-hospital-de-ermelino-matarazzo-2-765",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/delboni-auriemo-med-diag-hospital-liberdade-2-779",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/delboni-auriemo-med-diag-hospital-morumbi-2-780",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/delboni-auriemo-med-diag-hospital-samaritano-2-781",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/dgjr-2-788",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/esho-empresa-de-servicos-hospitalares-2-862",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/eye-care-laser-vision-centers-2-873",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/fertility-2-897",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/fl-analia-franco-2-916",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/fl-braz-leme-2-917",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/fl-rochavera-2-918",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/fleury-cerro-cora-2-919",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/fleury-medicina-e-saude-unid-hospital-samaritano-2-920",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/fleury-medicina-e-saude-unid-hospital-santo-antonio-2-921",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/fleury-medicina-e-saude-unidade-hospital-santa-catarina-2-922",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/fleury-medicina-e-saude-unidade-hospital-sao-luiz-jabaquara-2-923",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/fleury-medicina-e-saude-unidade-hospital-sirio-libanes-2-924",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/fleury-unidade-hospital-a-c-camargo-pires-da-mota-2-926",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/fpm-servicos-odontologicos-e-hospitalares-2-930",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/g-a-2-975",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/geah-grupo-especializado-em-anestesiologia-hospitalar-2-986",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/gen-servicos-medicos-hospitalares-2-988",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/global-med-servicos-medicos-e-hospitalares-2-995",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/grupo-rima-2-1011",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/h-olhos-2-1023",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/hat-psi-butanta-2-1033",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/hcloe-hospital-de-olhos-2-1056",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/hcloe-hospital-de-olhos-filial-1-2-1057",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/hcloe-hospital-de-olhos-filial-2-2-1058",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/home-care-cene-hospitallar-2-1176",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/home-care-enferlife-hospitalar-2-1180",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/hosp-9-de-julho-2-1210",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/hosp-anchieta-2-1211",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/hosp-augusto-barreira-2-1212",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/hosp-aviccena-2-1213",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/hosp-da-penha-2-1215",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/hosp-das-clinicaslab-de-investigacao-medica-2-1218",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/hosp-de-clinicas-j-helena-2-1219",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/hosp-e-mat-jardins-2-1220",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/hosp-evaldo-foz-2-1221",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/hosp-geral-de-sao-paulo-2-1223",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/hosp-independencia-2-1225",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/hosp-independencia-zona-lesteamb-2-1226",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/hosp-mat-8-de-maio-2-1227",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/hosp-mat-arabe-brasileiro-2-1228",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/hosp-mat-casa-verde-2-1229",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/hosp-mat-paranagua-2-1230",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/hosp-mat-sto-antonio-do-tucuruvi-2-1231",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/hosp-mat-v-carrao-2-1232",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/hosp-mat-vidas-2-1233",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/hosp-paulista-de-otorrinolaringologia-2-1239",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/hosp-ps-nova-iguatemi-2-1240",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/hosp-sao-conrado-2-1241",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/hosp-sto-amaro-2-1243",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/hosp-vera-cruz-2-1244",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/hospital-a-c-camargo-tamandare-2-1259",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/hospital-adventista-de-sao-paulo-2-1272",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/hospital-alemao-oswlado-cruz-2-1291",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/hospital-alvorada-chacara-flora-2-1303",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/hospital-alvorada-moema-2-1308",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/hospital-avape-2-1388",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/hospital-bosque-da-saude-2-1470",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/hospital-central-de-guaianases-2-1550",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/hospital-da-crianca-2-1634",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/hospital-da-face-2-1656",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/hospital-da-luz-2-1665",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/hospital-da-luz-113-2-1666",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/hospital-da-pele-2-1683",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/hospital-de-imunologia-dr-javier-2-2183",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/hospital-de-olhos-de-sao-paulo-unidade-leste-2-2272",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/hospital-de-olhos-de-sao-paulo-unidade-sul-2-2274",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/hospital-de-olhos-jardim-europa-ltda-2-2317",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/hospital-de-olhos-paulista-2-2333",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/hospital-dia-uno-2-2528",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/hospital-do-cabelo-2-2558",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/hospital-do-coracao-2-2577",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/hospital-do-coracao-jd-paulistano-2-2598",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/hospital-do-coracao-paraiso-abilio-soares-2-2599",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/hospital-do-dente-2-2605",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/hospital-dom-pedro-2-2674",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/hospital-e-casa-de-repouso-sainte-marie-2-2804",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/hospital-e-casa-de-repouso-sainte-marie-2-2805",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/hospital-e-casa-de-repouso-sainte-marie-2-2806",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/hospital-e-maternidade-metropolitano-2-2968",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/hospital-e-maternidade-santa-maria-2-3085",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/hospital-e-maternidade-sao-miguel-2-3140",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/hospital-e-maternidade-sao-rafael-sp-2-3146",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/hospital-e-pronto-atendimento-sancta-maggiore-2-3173",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/hospital-e-pronto-atendimento-sancta-maggiore-2-3174",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/hospital-e-pronto-atendimento-sancta-maggiore-2-3176",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/hospital-e-pronto-atendimento-sancta-maggiore-paris-2-3177",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/hospital-e-pronto-atendimento-sancta-maggiore-russia-2-3178",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/hospital-e-pronto-socorro-portinari-2-3188",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/hospital-esporte-e-saude-ltda-br-surgery-2-3239",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/hospital-geral-da-penha-2-3387",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/hospital-green-hill-2-3524",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/hospital-infantil-sabara-2-3598",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/hospital-ingles-2-3602",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/hospital-itaquera-2-3618",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/hospital-itatiaia-2-3619",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/hospital-leforte-2-3710",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/hospital-montemagno-2-4021",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/hospital-moriah-2-4025",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/hospital-next-butanta-2-5202",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/hospital-odontologico-24-hs-2-5348",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/hospital-oswaldo-cruz-2-5388",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/hospital-paulistano-2-5442",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/hospital-presidente-2-5493",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/hospital-sagrada-familia-2-5818",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/hospital-saint-patrick-2-5827",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/hospital-saint-paul-2-5828",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/hospital-saint-peter-2-5829",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/hospital-salt-lake-2-5830",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/hospital-samaritano-2-5840",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/hospital-samaritano-paulista-2-5857",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/hospital-san-gennaro-2-5861",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/hospital-sancta-maggiore-2-5864",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/hospital-sancta-maggiore-2-5865",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/hospital-sancta-maggiore-2-5866",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/hospital-sancta-maggiore-2-5867",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/hospital-sancta-maggiore-2-5868",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/hospital-santa-carmela-2-5883",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/hospital-santa-catarina-2-5897",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/hospital-santa-clara-2-5906",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/hospital-santa-paula-2-6023",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/hospital-santa-rita-2-6036",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/hospital-santa-virginia-2-6076",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/hospital-sao-camilo-ipiranga-2-6164",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/hospital-sao-camilo-pompeia-2-6167",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/hospital-sao-camilo-pompeia-2-2-6168",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/hospital-sao-camilo-santana-2-6169",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/hospital-sao-cristovao-clav-mooca-2-6178",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/hospital-sao-luiz-jabaquara-2-6455",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/hospital-sbc-2-6635",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/hospital-silvio-romero-2-6663",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/hospital-sirio-libanes-2-6668",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/hospital-sirio-libanes-unidade-brasil-2-6670",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/hospital-sirio-libanes-unidade-itaim-2-6671",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/hospital-sorocabana-2-6679",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/hospital-talita-2-6688",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/hospital-universitario-da-unifesp-hu-ii-2-6840",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/hospital-vidas-alta-complexidade-2-6905",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/hospital-vila-nova-star-2-6906",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/hospital-villa-lobos-2-6907",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/hospital-vitoria-2-6921",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/hospitalita-atend-domiciliar-2-6948",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/hsanp-hospital-2-6975",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/impar-servicos-hospitalares-filial-santa-paula-2-7017",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/impar-servicos-hospitalares-filial-santa-paula-oncologia-2-7018",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/in-care-hospital-de-reabilitacao-e-longa-permanencia-2-7022",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/incare-clinica-medica-de-transicao-2-7024",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/incare-hospital-de-transicao-2-7025",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/incare-hospital-de-transicao-ltda-2-7026",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/instituto-de-oncologia-santa-paula-2-7059",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/itau-ca-pinheiros-2-7104",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/itau-ca-tatuape-2-7105",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/itau-ceic-2-7106",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/itau-cto-2-7107",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/itau-itm-2-7108",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/itau-wtorre-2-7109",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/jfcl-clinica-de-medicina-hospitalar-2-7120",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/jm-servicos-medicos-e-hospitalares-2-7124",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/jml-servicos-hospitalares-2-7126",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/krbr-servicos-medicos-e-hospitalares-2-7134",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/lcl-servicos-medicos-hospitalares-2-7181",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/lifecare-assistencia-medica-domiciliar-e-hospitalar-2-7186",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/madrecare-retaguarda-hospitalar-2-7202",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/master-clin-2-7213",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/maternidade-santa-joana-2-7231",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/medina-servicos-medicos-e-hospitalares-2-7271",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/neo-telemedicina-2-7336",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/nespah-nucleo-especializado-em-anestesiologia-hospitalar-2-7342",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/next-hospital-santo-amaro-2-7347",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/ophthal-moema-2-7426",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/ophthal-santo-amaro-2-7427",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/ophthal-tatuape-2-7429",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/osl-servicos-medicos-hospitalares-2-7448",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/pe-esse-2-7465",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/pe-esse-2-7466",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/posto-de-coleta-do-hospital-nipo-brasileiro-2-7510",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/precordio-assist-medico-hospitalar-2-7523",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/premier-residence-hospital-2-7525",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/pro-matre-paulista-2-7537",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/proar-fisioterapia-2-7542",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/quimioterapia-no-hospital-samaritano-2-7586",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/r-cec-consultoria-e-gestao-hospitalar-2-7587",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/rp-consultoria-medica-e-hospitalar-2-7622",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/saha-servicos-medicos-e-hospitalares-2-7635",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/santa-marina-hospital-geral-e-maternidade-2-7681",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/sareh-2-7695",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/sempah-serv-med-especializados-em-anestesiologia-hospitalar-2-7721",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/servico-de-radioterapia-do-hospital-do-coracao-2-7733",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/servicos-medicos-hospitalares-santa-rita-2-7741",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/sim-hospital-dia-2-7777",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/st-casa-1-2-7849",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/st-casa-3-2-7850",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/st-sede-jk-2-7852",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/st-vsp-2-7853",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/star-life-2-7856",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/tacconi-servicos-medicos-e-hospitalares-2-7865",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/tamp-servicos-medicos-hospitalar-2-7867",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/tin-terapia-2-7876",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/unidade-ambulatorial-de-sustentabilidade-social-haoc-2-7905",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/unidade-avancada-barao-do-rio-branco-ii-2-7907",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/unidade-avancada-cubatao-hospital-da-luz-2-7908",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/unidade-avancada-einstein-ibirapuera-2-7911",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/unidade-avancada-einstein-perdizes-2-7912",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/unidade-de-reabilitacao-esporte-e-bem-estar-einstein-2-7923",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/unidade-diagnostica-2-7933",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/unidade-einstein-alto-de-pinheiros-2-7935",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/unidade-einstein-higienopolis-2-7941",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/unidade-einstein-parque-da-cidade-2-7942",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/unidade-einstein-safra-2-7945",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/unidade-einstein-telemedicina-2-7946",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/unidade-parque-ibirapuera-2-8069",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/unidade-vila-nova-2-8088",
    "https://postosdesaude.com.br/sp/sao-paulo/hospitais-particulares/victrice-2-8141"

]

nomes_hospitais = []
enderecos_hospitais = []
lista_servicos_hospitais = []

driver = webdriver.Chrome()

for link in lista_links:
    driver.get(link)

    nome_hospital = driver.find_element(By.CSS_SELECTOR, "h1[itemprop='name']").text

    endereco_hospital = driver.find_element(By.CSS_SELECTOR, "p[itemprop='address']").text

    servicos = driver.find_elements(By.CSS_SELECTOR, "table.table.tabelaServEspec tbody tr")
    servicos_hospital = []
    for servico in servicos:
        nome_servico = servico.find_element(By.CSS_SELECTOR, "td:nth-of-type(1)").text
        caracteristica_servico = servico.find_element(By.CSS_SELECTOR, "td:nth-of-type(2)").text
        servicos_hospital.append({"Nome do Serviço": nome_servico, "Característica": caracteristica_servico})

    nomes_hospitais.append(nome_hospital)
    enderecos_hospitais.append(endereco_hospital)
    lista_servicos_hospitais.append(servicos_hospital)

driver.quit()

lista_hospitais = []
for nome_hospital, endereco_hospital, servicos_hospital in zip(nomes_hospitais, enderecos_hospitais, lista_servicos_hospitais):
    for servico in servicos_hospital:
        lista_hospitais.append({"Nome": nome_hospital, "Endereço": endereco_hospital, "Serviço": servico})

dados_hospitais = pd.DataFrame(lista_hospitais)

dados_hospitais.to_excel("postos_particulares.xlsx", index=False)