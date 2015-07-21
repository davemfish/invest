"""Test Cases for CBC Model Functions.

python -m unittest test_cbc_model
"""

import unittest
import os
import pprint
import csv
import shutil

import numpy
from numpy import testing
import gdal

import natcap.invest.coastal_blue_carbon.utilities.io as io
import natcap.invest.coastal_blue_carbon.coastal_blue_carbon as cbc
from natcap.invest.coastal_blue_carbon.utilities.raster import Raster
from natcap.invest.coastal_blue_carbon.utilities.raster_factory import RasterFactory
from natcap.invest.coastal_blue_carbon.utilities.affine import Affine

pp = pprint.PrettyPrinter(indent=4)

NODATA_FLOAT = -16777216
NODATA_INT = -9999


def write_csv(filepath, l):
    f = open(filepath, 'wb')
    writer = csv.writer(f)
    for i in l:
        writer.writerow(i)


class TestCBCModel(unittest.TestCase):

    """Test cbc._set_initial_stock()."""

    def setUp(self):
        cwd = os.path.dirname(os.path.realpath(__file__))
        workspace = os.path.join(cwd, 'workspace')
        if not os.path.exists(workspace):
            os.mkdir(workspace)
        self.workspace = workspace
        self.results_suffix = ""

        table = [
            ['lulc-class', 'code', 'is_coastal_blue_carbon_habitat'],
            ['seagrass', '1', 'true'],
            ['man-made', '2', 'false'],
            ['marsh', '3', 'true'],
            ['mangrove', '4', 'true']]
        self.lulc_lookup_uri = os.path.join(self.workspace, 'lookup.csv')
        write_csv(self.lulc_lookup_uri, table)

        table = [
            ['lulc-class', 'seagrass', 'man-made', 'marsh', 'mangrove'],
            ['seagrass', 'accumulation', 'high-impact-disturbance', '', ''],
            ['man-made', 'accumulation', '', 'accumulation', ''],
            ['marsh', '', '', '', 'accumulation'],
            ['mangrove', '', '', '', '']]
        self.lulc_transition_uri = os.path.join(self.workspace, 'transition.csv')
        write_csv(self.lulc_transition_uri, table)

        shape = (2, 2)  # (2, 2)  #(1889, 1325)
        affine = Affine(30.0, 0.0, 443723.127328, 0.0, -30.0, 4956546.905980)
        proj = 26910
        datatype = gdal.GDT_Int32
        nodata_val = 255
        aoi_int_factory = RasterFactory(proj, datatype, nodata_val, shape[0], shape[1], affine=affine)
        year1_raster = aoi_int_factory.alternating(1, 2)
        year2_raster = aoi_int_factory.alternating(2, 1)
        year3_raster = aoi_int_factory.alternating(3, 1)
        year4_raster = aoi_int_factory.alternating(4, 1)
        self.lulc_snapshot_list = [
            year1_raster.uri,
            year2_raster.uri,
            year3_raster.uri,
            year4_raster.uri]

        self.lulc_snapshot_years_list = [2000, 2005, 2020, 2050]
        self.analysis_year = 2100

        table = [
            ['lulc-class', 'biomass', 'soil', 'litter'],
            ['seagrass', '1.0', '1.0', '0.5'],
            ['man-made', '0.0', '0.0', '0'],
            ['marsh', '2.0', '2.0', '1.0'],
            ['mangrove', '3.0', '3.0', '1.5']]
        self.carbon_pool_initial_uri = os.path.join(self.workspace, 'initial.csv')
        write_csv(self.carbon_pool_initial_uri, table)

        table = [
            ['lulc-class', 'pool', 'half-life', 'yearly_sequestration_per_ha', 'low-impact-disturbance', 'med-impact-disturbance', 'high-impact-disturbance'],
            ['seagrass', 'biomass', '1', '10', '0.1', '0.3', '0.7'],
            ['seagrass', 'soil', '2', '10', '0.1', '0.3', '0.7'],
            ['man-made', 'biomass', '0', '0', '0', '0', '0'],
            ['man-made', 'soil', '0', '0', '0', '0', '0'],
            ['marsh', 'biomass', '1', '20', '0.2', '0.4', '0.8'],
            ['marsh', 'soil', '2', '20', '0.2', '0.4', '0.8'],
            ['mangrove', 'biomass', '1', '30', '0.3', '0.5', '0.7'],
            ['mangrove', 'soil', '2', '30', '0.3', '0.5', '0.7']]
        self.carbon_pool_transient_uri = os.path.join(self.workspace, 'transient.csv')
        write_csv(self.carbon_pool_transient_uri, table)

        self.args = {
            'workspace': self.workspace,
            'results_suffix': self.results_suffix,
            'lulc_lookup_uri': self.lulc_lookup_uri,
            'lulc_transition_uri': self.lulc_transition_uri,
            'lulc_snapshot_list': self.lulc_snapshot_list,
            'lulc_snapshot_years_list': self.lulc_snapshot_years_list,
            'analysis_year': self.analysis_year,
            'carbon_pool_initial_uri': self.carbon_pool_initial_uri,
            'carbon_pool_transient_uri': self.carbon_pool_transient_uri,
        }

    def test_set_initial_stock(self):
        vars_dict = io.get_inputs(self.args)
        vars_dict = cbc._set_initial_stock(vars_dict)
        assert(vars_dict['total_carbon_stock_raster_list'][
            0].get_band(1)[0, 0] == 2.0)

    def test_run_transient_analysis(self):
        vars_dict = io.get_inputs(self.args)
        vars_dict = cbc._set_initial_stock(vars_dict)
        assert(vars_dict['total_carbon_stock_raster_list'][
            0].get_band(1)[0, 0] == 2.0)
        cbc._run_transient_analysis(vars_dict)
        print os.listdir(os.path.join(self.workspace, 'outputs'))

    def tearDown(self):
        shutil.rmtree(self.workspace)


if __name__ == '__main__':
    unittest.main()
