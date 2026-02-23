import click
import os
from dotenv import load_dotenv
import csv
from pathlib import Path

from graphql_client import GraphQLClient
from queries import TOP_8, HEADCOUNT
from parser import Parser
from analytics import Analytics
from exporter import Exporter

# Load environmental Variables
load_dotenv()
ENDPOINT_URL = os.getenv("ENDPOINT_URL")
if not ENDPOINT_URL:
    raise RuntimeError("GraphQL Endpoint is not set.")

API_KEY = os.getenv("API_KEY")
if not API_KEY:
    raise RuntimeError("API Key is not set.")

@click.group()
def cli():
    pass

@cli.command()
def top8():
    print("Running Top 8 Analytics...")
    client = GraphQLClient(ENDPOINT_URL, API_KEY)
    top8_nodes = client.fetch_tournament_info(TOP_8)
    top8Results = Parser.parse_top8(top8_nodes)
    top8Stats = Analytics.computeTop8Stats(top8Results)
    Exporter.export_top8_stats(top8Stats)
    print("Top 8 data has been exported.")


#headcount_nodes = client.fetch_tournament_info(HEADCOUNT)

if __name__ == "__main__":
    cli()