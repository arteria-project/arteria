import tempfile
from unittest.mock import patch
import yaml

from arteria.services.arteria_runfolder import main


@patch("arteria.services.arteria_runfolder.get_app")
@patch("aiohttp.web.run_app")
def test_cli_parameters(mock_run_app, mock_get_app):
    config = {"item": 1}
    with tempfile.NamedTemporaryFile(mode='w') as config_file:
        yaml.dump(config, config_file)
        with patch(
            "sys.argv",
            ["", "--config_file", config_file.name]
        ):
            main()

            mock_get_app.assert_called_with(config)
