# invoice
i am tired of invoicing SAAS that want me to pay them money each month. that's why i'm writing my own tool, just for my specific needs. it could be useful for other people at some point.

it's python again and will feature multiple export formats and overall json configurability.

i also take this project as an opportunity to check out http://mypy-lang.org/ .. feels pretty great so far.

## usage
    invoice new --help                    jwerner@manjaro
    usage: invoice new [-h] customer products [products ...]

    positional arguments:
      customer    customer shortname
      products    product shortname/s plus args

    optional arguments:
      -h, --help  show this help message and exit

## example
    invoice new hh taet2[start=13.11.14,end=15.11.14,price=400,place=Hamburg]
