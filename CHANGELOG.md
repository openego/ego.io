# Changelog
All notable changes to ego.io will be documented in this file.

The format is inpired from [Keep a Changelog](http://keepachangelog.com/en/1.0.0/)
and the versiong aim to respect [Semantic Versioning](http://semver.org/spec/v2.0.0.html).

Here is a template for new release sections

```
## [_._._] - 20XX-MM-DD

### Added
-
### Changed
-
### Removed
-
```
## [Unreleased]

### Added

### Changed

## [0.4.8] 2021-05-29

### Changed
- replace data type Numeric by Float(53) #86
- set default values for database connection details to oep connection details #83

## [0.4.7] 2019-08-29

### Changed
- fix installation problem when installing via pip #81

## [0.4.6] 2019-08-29

### Added
- CHANGELOG.md
- passwordless DB API engine to access the OpenEnergy Platform via
oedialect #79

### Changed
- upper bounds for sqlalchemy and geoalchemy2 removed (due to incompatibilities
with depending packages) #72 #73
- psycopg2 replaced by by psycopg2-binary #75
- ORM update #74
- fix v0.4.5 installation problem #78
- add oedialect to dependencies #70 

## Prior releases

There's no changelog for releases prior to v0.4.6. Check out the
[releases](https://github.com/openego/ego.io/releases) on github.
