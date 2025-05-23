import hydra
import pyscripts.schema as schema
import pyscripts.parser as parser
import utils.logger as logger

@hydra.main(config_path="./config/", config_name="config", version_base="1.3")
def main(config: schema.Config):
    args = parser.get_args()
    config.merge_with(args)

if __name__ == "__main__":
    main()