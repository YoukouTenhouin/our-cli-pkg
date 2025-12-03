# Example repository for an OUR package

This repository serves as an example for [OUR](https://hackweek.opensuse.org/25/projects/our-opensuse-user-repositiory).

## Usage

This repository can be build with [our-cli](https://github.com/YoukouTenhouin/our-cli). To do that, you can:

- Checkout both repositories

- Build our-cli with:
```
$ cd <our-cli repo>
$ cargo build
```

- Build this repository with our-cli:
```
$ cd <this repo>
$ <our-cli repo>/target/debug/our build our-cli.spec
```

Now you should have our-cli built and installed on your system:

```
$ our help
```
