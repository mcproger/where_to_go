# Where to go
An educational project for the https://dvmn.org course.
The hosted version can be found [here]()

![map](https://raw.githubusercontent.com/mcproger/where_to_go/master/docs/README.png)

Test data were taken from [KudaGo](https://kudago.com/)

## Sections

* [Map with places]()
* [Admin panel]()
* [API endpoing]()

## Configuration

Configuration is stored in src/app/.env, for examples see src/app/.env.ci

## Installation

This project requires python3.10 and Django4

```
make install
cd src
cp app/.env.ci app/.env  # default environment variables
make migrations
make migrate
make run
```

To create superuser for the admin panel use `make superuser`


## Testing

`make lint && make test`


## Dependencies

To update dependencies, add the new one to the `requirements.in` file and run

```
make freeze
```

See the `Makefile` for the full list of available commands
