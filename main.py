from flask import Flask, render_template, request, Response
app = Flask(__name__)

import pandas as pd

gdfRip = pd.read_file(url_for('static', filename='pandas/RipGeo01012021_WGS84.shp'))
gdfReg = pd.read_file(url_for('static', filename='pandas/Reg01012021_WGS84.shp'))
gdfProv = pd.read_file(url_for('static', filename='pandas/ProvCM01012021_WGS84.shp'))
gdfCom = pd.read_file(url_for('static', filename='pandas/Com01012021_WGS84.shp'))

@app.route('/', methods=['GET'])
def elenco_ripartizioni():
    return render_template('url_elencoRip.html', nomi=gdfRip['DEN_RIP'].to_list(), codici=gdfRip['COD_RIP'].to_list())

@app.route('/regioni', methods=['GET'])
def regioni():
    gdfRegioni = gdfReg[gdfReg['COD_RIP']==int(request.args['id'])]
    return render_template('url_elencoReg.html', nomi=gdfRegioni['DEN_REG'].to_list(), codici=gdfRegioni['COD_REG'].to_list())


@app.route('/province', methods=['GET'])
def province():
    gdfProvince = gdfProv[gdfProv['COD_REG']==int(request.args['id'])].sort_values(by='DEN_UTS')
    return render_template('url_elencoProv.html', nomi=gdfProvince['DEN_UTS'].to_list(), codici=gdfProvince['COD_PROV'].to_list())

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)