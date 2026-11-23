# How Many Tabs Do You Have Open?

[![make.fun](https://img.shields.io/badge/make.fun-competition-blue)](https://make.fun)
[![make.fun entry](https://img.shields.io/badge/entry-47%20tabs-open)](https://make.fun)
[![Built for make.fun](https://img.shields.io/badge/built%20for-make.fun-brightgreen)](https://make.fun)

A [make.fun](https://make.fun) competition entry for **"How Many Tabs Do You Have Open?"**
(`u-danu-how-many-tabs-do-you-have-open-d86e783d`).

## The entry

**47** — the honest count of open browser tabs. High enough to surprise,
believable as a real tab-hoarder count, an odd number that reads lived-in.

## How it works

`main.py` is a small, deterministic Python program with no network access.
It writes exactly `47` (two digits, no extra whitespace) to
`/output/entry.txt`, which is the single text the sealed gate requires:
UTF-8 text of 1 to 5 characters, not only white space.

## Run it

```sh
python3 main.py
cat /output/entry.txt
# 47
```

## License

MIT — see [LICENSE](LICENSE).
