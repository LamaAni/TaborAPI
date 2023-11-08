from tabor_api.config import TaborConfig, load_config
from tabor_api.exceptions import TaborClientException
from tabor_api.visa.interface import TEVisaInst


class TaborClient:
    def __init__(
        self,
        client: TEVisaInst = None,
        config: TaborConfig = None,
    ) -> None:
        self.client = client
        self.config = config or load_config()

    def connect(self):
        assert self.client is None, TaborClientException("Client was already conncted")
        inst_addr = (
            f"TCPIP::{self.config.visa_host_address}::{self.config.visa_port}::SOCKET"
        )
        self.client = TEVisaInst(inst_addr)  # get instruent pointer
        # assert connect
        self.client.send_scpi_query("*IDN?")

    def disconnect(self):
        assert self.client, TaborClientException(
            "Client not connected or dose not exist"
        )
        self.client.close_instrument()

    def query(self, query: str):
        self.client.send_scpi_query(query)

    GLOBAL_CLIENT: "TaborClient" = None

    @property
    @classmethod
    def client(cls):
        """The global client"""
        if cls.GLOBAL_CLIENT is None:
            cls.GLOBAL_CLIENT = TaborClient()
            cls.GLOBAL_CLIENT.connect()
        return cls.GLOBAL_CLIENT
