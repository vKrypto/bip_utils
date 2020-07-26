# Copyright (c) 2020 Emanuele Bellocchia
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.


# Imports
import unittest
from bip_utils        import Bip44, Bip44Coins
from .test_bip44_base import Bip44BaseTestHelper


# Results generated with Ian Coleman web page:
# https://iancoleman.io/bip39/
# There are some differences from the website and the specs I found for Litecoin testnet (extended keys prefixes) so,
# in that case, the keys were generated by this library after begin tested for the correct addresses
TEST_VECT = \
    [
        # Bitcoin
        {
            "coin"       : Bip44Coins.BITCOIN,
            "names"      : ("Bitcoin", "BTC"),
            "is_testnet" : False,
            "seed"       : b"5eb00bbddcf069084889a8ab9155568165f5c453ccb85e70811aaed6f6da5fc19a5ac40b389cd370d086206dec8aa6c43daea6690f20ad3d8d48b2d2ce9e38e4",
            "ex_master"  :  "xprv9s21ZrQH143K3GJpoapnV8SFfukcVBSfeCficPSGfubmSFDxo1kuHnLisriDvSnRRuL2Qrg5ggqHKNVpxR86QEC8w35uxmGoggxtQTPvfUu",
            "wif_master" :  "5HzxC8XHHAtoC5jVvScY8Tr99Ud9MwFdF2pJKYsMTUknJZEurYr",
            "account" :
                {
                    "ex_pub"  : "xpub6BosfCnifzxcFwrSzQiqu2DBVTshkCXacvNsWGYJVVhhawA7d4R5WSWGFNbi8Aw6ZRc1brxMyWMzG3DSSSSoekkudhUd9yLb6qx39T9nMdj",
                    "ex_priv" : "xprv9xpXFhFpqdQK3TmytPBqXtGSwS3DLjojFhTGht8gwAAii8py5X6pxeBnQ6ehJiyJ6nDjWGJfZ95WxByFXVkDxHXrqu53WCRGypk2ttuqncb",
                },
            "chain_ext" :
                {
                    "ex_pub"  : "xpub6ELHKXNimKbxMCytPh7EdC2QXx46T9qLDJWGnTraz1H9kMMFdcduoU69wh9cxP12wDxqAAfbaESWGYt5rREsX1J8iR2TEunvzvddduAPYcY",
                    "ex_priv" : "xprvA1Lvv1qpvx3f8iuRHfaEG45fyvDc3h7Ur5afz5SyRfkAsZ2765KfFfmg6Q9oEJDgf4UdYHphzzJybLykZfznUMKL2KNUU8pLRQgstN5kmFe",
                },
            "addresses" :
                [
                    "1LqBGSKuX5yYUonjxT5qGfpUsXKYYWeabA",
                    "1Ak8PffB2meyfYnbXZR9EGfLfFZVpzJvQP",
                    "1MNF5RSaabFwcbtJirJwKnDytsXXEsVsNb",
                    "1MVGa13XFvvpKGZdX389iU8b3qwtmAyrsJ",
                    "1Gka4JdwhLxRwXaC6oLNH4YuEogeeSwqW7",
                ],
        },
        # Bitcoin
        {
            "coin"       : Bip44Coins.BITCOIN_CASH,
            "names"      : ("Bitcoin Cash", "BCH"),
            "is_testnet" : False,
            "seed"       : b"5eb00bbddcf069084889a8ab9155568165f5c453ccb85e70811aaed6f6da5fc19a5ac40b389cd370d086206dec8aa6c43daea6690f20ad3d8d48b2d2ce9e38e4",
            "ex_master"  :  "xprv9s21ZrQH143K3GJpoapnV8SFfukcVBSfeCficPSGfubmSFDxo1kuHnLisriDvSnRRuL2Qrg5ggqHKNVpxR86QEC8w35uxmGoggxtQTPvfUu",
            "wif_master" :  "5HzxC8XHHAtoC5jVvScY8Tr99Ud9MwFdF2pJKYsMTUknJZEurYr",
            "account" :
                {
                    "ex_pub"  : "xpub6ByHsPNSQXTWZ7PLESMY2FufyYWtLXagSUpMQq7Un96SiThZH2iJB1X7pwviH1WtKVeDP6K8d6xxFzzoaFzF3s8BKCZx8oEDdDkNnp4owAZ",
                    "ex_priv" : "xprv9xywTsqYa9uDLdJs8QpXf7xwRWgPw4rq5FtkcShsDoZTqfNQjVQ3dDCdyedXX3FqB18U8e8PfVMeFqkhzPGseKVMDjGe5rPdiUXMxy7BQNJ",
                },
            "chain_ext" :
                {
                    "ex_pub"  : "xpub6F2iaK2JUPcgrZ6RTGH6t8VybLPu1XzfrHsDsaKvK6NfULznU6i6aw6ZoefDW2DpNruSLw73RwQg46qvpqB3eryeJJ2tkFCF4Z6gbr8Pjja",
                    "ex_priv" : "xprvA23NAoVQe24Pe51xMEk6WzZF3JZQc5GpV4wd5BvJkkqgbYfdvZPr38n5xR8cpzWJ6AjAnLRYVcqLWMsCHghvCdQTtcZm9HWTStmvYiT7BTC",
                },
            "addresses_legacy" :
                [
                    "1mW6fDEMjKrDHvLvoEsaeLxSCzZBf3Bfg",
                    "18Cp2ivkLHyJwHMm9NzDRBh6Gi7m4MC2we",
                    "15Ax9BJRJ4TABF85UsPpz9QvuBpiJhCfsw",
                    "1H53u5dU1axLgun9VxUjQZMBMxW65DazhB",
                    "18rTBsgLJosVgZodepiQ1wFoGFhhMK3iwL",
                ],
            "addresses" :
                [
                    "bitcoincash:qqyx49mu0kkn9ftfj6hje6g2wfer34yfnq5tahq3q6",
                    "bitcoincash:qp8sfdhgjlq68hlzka9lcsxtcnvuvnd0xqxugfzzc5",
                    "bitcoincash:qqkuy34ntrye9a2h4xpdstcu4aq5wfrwscjtaphenr",
                    "bitcoincash:qzcyvxr0e23d408u62ulf6cnspc0k4dyduy8kh77nc",
                    "bitcoincash:qptzx8m39zjuuyvrf86s3kywuledfht2jcty8we6gv",
                ],
        },
        # BitcoinSV
        {
            "coin"       : Bip44Coins.BITCOIN_SV,
            "names"      : ("BitcoinSV", "BSV"),
            "is_testnet" : False,
            "seed"       : b"5eb00bbddcf069084889a8ab9155568165f5c453ccb85e70811aaed6f6da5fc19a5ac40b389cd370d086206dec8aa6c43daea6690f20ad3d8d48b2d2ce9e38e4",
            "ex_master"  :  "xprv9s21ZrQH143K3GJpoapnV8SFfukcVBSfeCficPSGfubmSFDxo1kuHnLisriDvSnRRuL2Qrg5ggqHKNVpxR86QEC8w35uxmGoggxtQTPvfUu",
            "wif_master" :  "5HzxC8XHHAtoC5jVvScY8Tr99Ud9MwFdF2pJKYsMTUknJZEurYr",
            "account" :
                {
                    "ex_pub"  : "xpub6CdMDgU2hzWyeZ852LWqp5AfDz3ty2cRfi4jEw9BT8aNYugMQvVykQsKLARZdbqKKp7yTviJdL1N9saYLmJNKD1rwVAwLTmU8r8qKeoyG4R",
                    "ex_priv" : "xprv9ydzpAw8scxgS53bvJyqSwDvfxDQZZtaJV98SYjZto3Pg7MCsPBjCcYqUtnWPRNayEXUcSYZDvXux545bHZwda7YUWvReJiRkx38VXathgK",
                },
            "chain_ext" :
                {
                    "ex_pub"  : "xpub6F4QRDXQLHsQatQpTvCAz7tiRZvKUj74BpUXYL4DneDnCGxtdGo44BUWQtGy2wAotFE6t6cB3kDEWbnxqaEdVdg3bb3uLRECKkBnnK1pdzQ",
                    "ex_priv" : "xprvA2541hzWVvK7NQLMMtfAcywysY5q5GPCpbYvjwecEJgoKUdk5jUoWPA2ZcJDkGmD3Fg2cVpmafjqJsVrdPPKq5cQ7cVyz2yQZrg4ceRnTXo",
                },
            "addresses" :
                [
                    "1K6LZdwpKT5XkEZo2T2kW197aMXYbYMc4f",
                    "1DhquSu6ky8QQnf88b1d3tRYeUkMLASZg9",
                    "155Vurs4bMMu5BemtZ6cVPhryGWef4VxZu",
                    "1MgmeSFC4F5L8idUUW7fSL7QFfwbxJaW8B",
                    "1D4eJS94heKPtAaU5jcfecMEk5i1vzEvAo",
                ],
        },
        # Litecoin
        {
            "coin"          : Bip44Coins.LITECOIN,
            "names"         : ("Litecoin", "LTC"),
            "is_testnet"    : False,
            "seed"          : b"5eb00bbddcf069084889a8ab9155568165f5c453ccb85e70811aaed6f6da5fc19a5ac40b389cd370d086206dec8aa6c43daea6690f20ad3d8d48b2d2ce9e38e4",
            "ex_master"     :  "xprv9s21ZrQH143K3GJpoapnV8SFfukcVBSfeCficPSGfubmSFDxo1kuHnLisriDvSnRRuL2Qrg5ggqHKNVpxR86QEC8w35uxmGoggxtQTPvfUu",
            "ex_master_alt" :  "Ltpv71G8qDifUiNetExQFUsQdYezsBDUaB814BhGZsphfZBrT3zqfeXTed3NqdFEoARcM1uJVNKbqmXwJscuMY753LZUtc36GiKqV5anTrnqWfr",
            "wif_master"    :  "6uJgfG4pBbMffTdMSGQVurdK6xBcZjhf1iDU2jtPAw5PzRdhx9m",
            "account" :
                {
                    "ex_pub"      : "xpub6BnJJjq783EdyBeQPA9P9ao9DTS3fUqyKG5NJDcrCiwwxEkesGoHN94LZRGE7rz1jgcvmmp8j55BNx573KFq1WBwKiemzkdfNKffKx6Mvku",
                    "ex_priv"     : "xprv9xnwuEJDHfgLkhZwH8cNnSrQfRbZG287x39mVqDEePQy5SRWKjV2pLjri8x93UfBSQdsGPeJFi8qXKexJUNj5eU3gEKfHUzo6EmuK6CSgEq",
                    "ex_pub_alt"  : "Ltub2YDQmP391UYeDYvLye9P1SuNJFkcRGN7SYHM8JMxaDnegcPTXHJ2BnYmvHnFnGPGKu2WMuCga6iZV3SDxDMGrRyMcrYEfSPhrpS1EPkC43E",
                    "ex_priv_alt" : "Ltpv7735AbcbmL1gbgDWj2ezvs59rh4RM1oTN2BKTKbfe3146FCPCNFbBBSWfuV9vCJNMXD9LuHpQnqVWpn2hbMhikqPdoGqbS3ptdPoNWEvvgR",
                },
            "chain_ext" :
                {
                    "ex_pub"      : "xpub6F8vdBLe2hjJ6hn9Mh7gH4dGQrUvWy8TSoNWPF1Kz1sbcmzdDQDTRZKoWGdxDyF4K2bDnKYmzb3oLWiMGnghLxwv3qywBcDJy2PLuX86BML",
                    "ex_priv"     : "xprvA29aDfokCLAztDhgFfafuvgXrpeS7WQc5aSuarbiRgLcjyfUfruCsm1KezybgSj2V3g4rxmfJ3bKyLxtmRk8rLtUgLu8Ta8j3fdLG5n9RSV",
                    "ex_pub_alt"  : "Ltub2ba35pYfv93JM545xB7g8vjVVeoVGkeba5aVDKkSMWiJM9dRsQiCFCpEs99ytNeJuEzoNSwKqchBSc5UBgn9BtjLLysPrHyMTX9gp7D46dD",
                    "ex_priv_alt" : "Ltpv7APhV388fzWLjCMFhZdJ4LuH467JCW5wVZUTYLz9RKvhknSMYVfmEbhycmWcZANDQAFLwURBT8Hyxr5yAYj7VTFpdurJmXBkr4FEKVQPVMv",
                },
            "addresses" :
                [
                    "LUWPbpM43E2p7ZSh8cyTBEkvpHmr3cB8Ez",
                    "Ldatw8ZjgMGNUo5HMN6RgCrjmh7q494Si3",
                    "LX4YojYdeBk3TtUcryCcgAqYxjicKfK7AD",
                    "LgbbqoBcNc8voAvrrk3ZyqCU3Y4H24aauc",
                    "LiNDwbwBhX9djY7tb3gWvrXjuWQNerLjnP",
                ],
        },
        # Dogecoin
        {
            "coin"       : Bip44Coins.DOGECOIN,
            "names"      : ("Dogecoin", "DOGE"),
            "is_testnet" : False,
            "seed"       : b"5eb00bbddcf069084889a8ab9155568165f5c453ccb85e70811aaed6f6da5fc19a5ac40b389cd370d086206dec8aa6c43daea6690f20ad3d8d48b2d2ce9e38e4",
            "ex_master"  :  "dgpv51eADS3spNJh98bWAfYnAW8K1gMy86HKmH1dpyT8kLsUKBqssT3jsLLFWyK4zbruL51UjejFDzrFzBcwjjA57rSv6D2978QigKG4xbCfJV6",
            "wif_master" :  "6JKHV5zEqwBbEhAf7qEWk5qNcu6gs4XtrCwXe3WFH8xR7BcSCbr",
            "account" :
                {
                    "ex_pub"  : "dgub8rUhDtD3YFGZTUphBfpBbzvFxSMKQXYLzg87Me2ta78r2SdVLmypBUkkxrrn9RTnchsyiJSkHZyLWxD13ibBiXtuFWktBoDaGaZjQUBLNLs",
                    "ex_priv" : "dgpv57bftCH9z6cEAdAY9SCDV9NfVsygaQWdi5LuCXdumz5qUPWnw1S3YBM7PdHXMvA8oSGS6Pbes1xEHMd5Zi2qHVK45y5FKKXzBXsZcTtYmX5",
                },
            "chain_ext" :
                {
                    "ex_pub"  : "dgub8toY7HgJc8TXA6fsb32FeTVrnqYMsBghLkw1Bu1XeDVJRun2YmnQTJUcNFPfcNs6Kf14DJo1gfKMFucNbdwQweXU1qknNHmTQfLKQLQTaS1",
                    "ex_priv" : "dgpv59vWmbkR3yoBsF1iYoQHXbxGLHAj34ez4A9o2ncYr6SHsrfL91Edp14xo29tx1a3cZA5M3o3fbr6g3ZViHrHkgSVE3WNJ23jgESJtkkL7hs",
                },
            "addresses" :
                [
                    "DBus3bamQjgJULBJtYXpEzDWQRwF5iwxgC",
                    "DAcDAtJRztxBHyA6D6h8du1HguyTR43Mas",
                    "D8K3KyDQ9FXeC3ADCuWW7cnWC7RvjHjV8H",
                    "D6RRdXkUbb3pazkYGXAXwbJY5iC8Tyqwzh",
                    "DTdrvUHbk5oMyi62tM7LqrjAcXfqB7eaad",
                ],
        },
        # Dash
        {
            "coin"       : Bip44Coins.DASH,
            "names"      : ("Dash", "DASH"),
            "is_testnet" : False,
            "seed"       : b"5eb00bbddcf069084889a8ab9155568165f5c453ccb85e70811aaed6f6da5fc19a5ac40b389cd370d086206dec8aa6c43daea6690f20ad3d8d48b2d2ce9e38e4",
            "ex_master"  :  "xprv9s21ZrQH143K3GJpoapnV8SFfukcVBSfeCficPSGfubmSFDxo1kuHnLisriDvSnRRuL2Qrg5ggqHKNVpxR86QEC8w35uxmGoggxtQTPvfUu",
            "wif_master" :  "7qjXbkdi3WJ1SRu6pVnUcqQzk9RimTJB3cCUrw9V1HGFoqaB948",
            "account" :
                {
                    "ex_pub"  : "xpub6CYEjsU6zPM3sADS2ubu2aZeGxCm3C5KabkCpo4rkNbXGAH9M7rRUJ4E5CKiyUddmRzrSCopPzisTBrXkfCD4o577XKM9mzyZtP1Xdbizyk",
                    "ex_priv" : "xprv9yYtLMwDA1nkeg8xvt4tfScuivNGdjMUDNpc2QfFC34YPMwzoaYAvVjkDvJ1APVeGMJnbJ6gPZMq4G7UfExoP5PpAS3UCF9utjeWa5eXq23",
                },
            "chain_ext" :
                {
                    "ex_pub"  : "xpub6FKQUVtZJMKhDeyeLuVTXT9UzGYy1hLn6rBSEdDbuCbpRsTytXimeU1kS2ai17SuC29cx43Q7RtmL9SGG22PqMdb36EGWKbUS3meW9sWdEm",
                    "ex_priv" : "xprvA2L44zMfTymQ1AuBEsxTAKCkSEiUcEcvjdFqSEozLs4qZ58qLzQX6fhGanTTqMrwQevXCq3NUSw4xncudnC4s6htZkGBzJWMyG7LFgy4Kvs",
                },
            "addresses" :
                [
                    "XoJA8qE3N2Y3jMLEtZ3vcN42qseZ8LvFf5",
                    "XbctnEsgWTn5j1co3emZynemxSFPqkLRKZ",
                    "XdD2biTJ3saZtcR6ravwJ9bvmkvmDq49Xg",
                    "XkBrNhE8srfb8BbeTRSU4dxWsjjedra4Xn",
                    "Xe8n8PZNgngjbMCFEA9unH26TmEWPPjm6a",
                ],
        },
        # Ethereum
        {
            "coin"       : Bip44Coins.ETHEREUM,
            "names"      : ("Ethereum", "ETH"),
            "is_testnet" : False,
            "seed"       : b"5eb00bbddcf069084889a8ab9155568165f5c453ccb85e70811aaed6f6da5fc19a5ac40b389cd370d086206dec8aa6c43daea6690f20ad3d8d48b2d2ce9e38e4",
            "ex_master"  :  "xprv9s21ZrQH143K3GJpoapnV8SFfukcVBSfeCficPSGfubmSFDxo1kuHnLisriDvSnRRuL2Qrg5ggqHKNVpxR86QEC8w35uxmGoggxtQTPvfUu",
            "wif_master" :  "",
            "account" :
                {
                    "ex_pub"  : "xpub6DCoCpSuQZB2jawqnGMEPS63ePKWkwWPH4TU45Q7LPXWuNd8TMtVxRrgjtEshuqpK3mdhaWHPFsBngh5GFZaM6si3yZdUsT8ddYM3PwnATt",
                    "ex_priv" : "xprv9zDSoJv1aBcjX6sNgEpE2J9K6MV2MUnXuqXsFgzVn3zY2aHyupaFQdYCtdCbNMkvcTdx9FeN49sgXw6mjrhrFLRSzJVnRYPfSCCgjeg4GxY",
                },
            "chain_ext" :
                {
                    "ex_pub"  : "xpub6EF8jXqFeFEW5bwMU7RpQtHkzE4KJxcqJtvkCjJumzW8CPpacXkb92ek4WzLQXjL93HycJwTPUAcuNxCqFPKKU5m5Z2Vq4nCyh5CyPeBFFr",
                    "ex_priv" : "xprvA1FnL2JMosgCs7rtN5tp3kM2SCDpuVtywg19QLuJDey9KbVS4zSLbELGDFdugxESvYxCU1wEJhDmMXvHKwmpCLd8QSoUJCHmVHCGvpFPxiw",
                },
            "addresses" :
                [
                    "0x9858EfFD232B4033E47d90003D41EC34EcaEda94",
                    "0x6Fac4D18c912343BF86fa7049364Dd4E424Ab9C0",
                    "0xb6716976A3ebe8D39aCEB04372f22Ff8e6802D7A",
                    "0xF3f50213C1d2e255e4B2bAD430F8A38EEF8D718E",
                    "0x51cA8ff9f1C0a99f88E86B8112eA3237F55374cA",
                ],
        },
        # Ripple
        {
            "coin"       : Bip44Coins.RIPPLE,
            "names"      : ("Ripple", "XRP"),
            "is_testnet" : False,
            "seed"       : b"5eb00bbddcf069084889a8ab9155568165f5c453ccb85e70811aaed6f6da5fc19a5ac40b389cd370d086206dec8aa6c43daea6690f20ad3d8d48b2d2ce9e38e4",
            "ex_master"  :  "xprv9s21ZrQH143K3GJpoapnV8SFfukcVBSfeCficPSGfubmSFDxo1kuHnLisriDvSnRRuL2Qrg5ggqHKNVpxR86QEC8w35uxmGoggxtQTPvfUu",
            "wif_master" :  "",
            "account" :
                {
                    "ex_pub"  : "xpub6CFKyZTfzj3cyeRLUDKwQQ5s1tqTTdVgywKMVkrB2i1taGFbhazkxDzWVsfBHZpv7rg6qpDBGYR5oA8iazEfa44CdQkkknPFHJ7YCzncCS9",
                    "ex_priv" : "xprv9yFya3vnAMVKmALsNBnw3G98Trzy4AmqciPkhNSZUNUuhTvTA3gWQRg2ecJFS3PDLsfYFgwDW1UukaapjTDUENfiwg22ryd4mWiph8Faw3p",
                },
            "chain_ext" :
                {
                    "ex_pub"  : "xpub6F119CdfnfeSVeXbJG7h88TG6SjjtvFYBup7HszDLmaCCDgbZ4n1tP6J6R8PikUqtiqgdJSXXB79V3SxVA4LkygGDkesJ4pW5bq3dQU7cbm",
                    "ex_priv" : "xprvA21ejh6mxJ69HAT8CEagkzWXYQuFVTXgpgtWVVabnS3DKRMT1XTmLampF9DgbLwYuqZAZCHMokjt2rCCMnScQLZWmHdnS11XfySXtiA5ygo",
                },
            "addresses" :
                [
                    "rHsMGQEkVNJmpGWs8XUBoTBiAAbwxZN5v3",
                    "r3AgF9mMBFtaLhKcg96weMhbbEFLZ3mx17",
                    "r4Sh61HP7nxB6mQxXSSeN2DCkG3sTrzb2c",
                    "rwT7dzQuZim2SdY1jGFGwpre4bh6xpr31a",
                    "rPdQVkTzpZ7ToRqTRBRrUKPoCTty7n3UVj",
                ],
        },
        # Bitcoin test net
        {
            "coin"       : Bip44Coins.BITCOIN_TESTNET,
            "names"      : ("Bitcoin TestNet", "BTC"),
            "is_testnet" : True,
            "seed"       : b"5eb00bbddcf069084889a8ab9155568165f5c453ccb85e70811aaed6f6da5fc19a5ac40b389cd370d086206dec8aa6c43daea6690f20ad3d8d48b2d2ce9e38e4",
            "ex_master"  :  "tprv8ZgxMBicQKsPe5YMU9gHen4Ez3ApihUfykaqUorj9t6FDqy3nP6eoXiAo2ssvpAjoLroQxHqr3R5nE3a5dU3DHTjTgJDd7zrbniJr6nrCzd",
            "wif_master" :  "91mamsLpsPxwA9EnYnWT14Q6o8yrX6npaygFQBDroDVq5dZG3q3",
            "account" :
                {
                    "ex_pub"  : "tpubDC5FSnBiZDMmhiuCmWAYsLwgLYrrT9rAqvTySfuCCrgsWz8wxMXUS9Tb9iVMvcRbvFcAHGkMD5Kx8koh4GquNGNTfohfk7pgjhaPCdXpoba",
                    "ex_priv" : "tprv8fPDJN9UQqg6pFsQsrVxTwHZmXLvHpfGGcsCA9rtnatUgVtBKxhtFeqiyaYKSWydunKpjhvgJf6PwTwgirwuCbFq8YKgpQiaVJf3JCrNmkR",
                },
            "chain_ext" :
                {
                    "ex_pub"  : "tpubDEQBfiy13hMZzGT4NWqNnaSWwVqYQ58kuu2pDYjkrf8F6DLKAprm8c65Pyh7PrzodXHtJuEXFu5yf6JbvYaL8rz7v28zapwbuzZzr7z4UvR",
                    "ex_priv" : "tprv8hi9XJvkuKfu6oRGUsAnPAnQNUKcEjwrLbS2w2hTSPKrFj5YYS3Ax7UDDrZZHd4PSnPLW5whNxAXTW5bBrSNiSD1LUeg9n4j5sdGRJsZZwP",
                },
            "addresses" :
                [
                    "mkpZhYtJu2r87Js3pDiWJDmPte2NRZ8bJV",
                    "mzpbWabUQm1w8ijuJnAof5eiSTep27deVH",
                    "mnTkxhNkgx7TsZrEdRcPti564yQTzynGJp",
                    "mpW3iVi2Td1vqDK8Nfie29ddZXf9spmZkX",
                    "n2BMo5arHDyAK2CM8c56eoEd18uEkKnRLC",
                ],
        },
        # Bitcoin Cash test net
        {
            "coin"       : Bip44Coins.BITCOIN_CASH_TESTNET,
            "names"      : ("Bitcoin Cash TestNet", "BCH"),
            "is_testnet" : True,
            "seed"       : b"5eb00bbddcf069084889a8ab9155568165f5c453ccb85e70811aaed6f6da5fc19a5ac40b389cd370d086206dec8aa6c43daea6690f20ad3d8d48b2d2ce9e38e4",
            "ex_master"  :  "tprv8ZgxMBicQKsPe5YMU9gHen4Ez3ApihUfykaqUorj9t6FDqy3nP6eoXiAo2ssvpAjoLroQxHqr3R5nE3a5dU3DHTjTgJDd7zrbniJr6nrCzd",
            "wif_master" :  "91mamsLpsPxwA9EnYnWT14Q6o8yrX6npaygFQBDroDVq5dZG3q3",
            "account" :
                {
                    "ex_pub"  : "tpubDC5FSnBiZDMmhiuCmWAYsLwgLYrrT9rAqvTySfuCCrgsWz8wxMXUS9Tb9iVMvcRbvFcAHGkMD5Kx8koh4GquNGNTfohfk7pgjhaPCdXpoba",
                    "ex_priv" : "tprv8fPDJN9UQqg6pFsQsrVxTwHZmXLvHpfGGcsCA9rtnatUgVtBKxhtFeqiyaYKSWydunKpjhvgJf6PwTwgirwuCbFq8YKgpQiaVJf3JCrNmkR",
                },
            "chain_ext" :
                {
                    "ex_pub"  : "tpubDEQBfiy13hMZzGT4NWqNnaSWwVqYQ58kuu2pDYjkrf8F6DLKAprm8c65Pyh7PrzodXHtJuEXFu5yf6JbvYaL8rz7v28zapwbuzZzr7z4UvR",
                    "ex_priv" : "tprv8hi9XJvkuKfu6oRGUsAnPAnQNUKcEjwrLbS2w2hTSPKrFj5YYS3Ax7UDDrZZHd4PSnPLW5whNxAXTW5bBrSNiSD1LUeg9n4j5sdGRJsZZwP",
                },
            "addresses_legacy" :
                [
                    "mkpZhYtJu2r87Js3pDiWJDmPte2NRZ8bJV",
                    "mzpbWabUQm1w8ijuJnAof5eiSTep27deVH",
                    "mnTkxhNkgx7TsZrEdRcPti564yQTzynGJp",
                    "mpW3iVi2Td1vqDK8Nfie29ddZXf9spmZkX",
                    "n2BMo5arHDyAK2CM8c56eoEd18uEkKnRLC",
                ],
            "addresses" :
                [
                    "bchtest:qqaz6s295ncfs53m86qj0uw6sl8u2kuw0ymst35fx4",
                    "bchtest:qrfuppcw3cf6nmpjpufgpzy3y74ptfxq5yxdy864k4",
                    "bchtest:qpxzu2ljsp5sgk5wkcnusw0lyvrtwwa6xq7ysu5t02",
                    "bchtest:qp3g60wa822p8xp6padds48mrs8c0ywd2g7nk9ff45",
                    "bchtest:qr32turulady0gcxhah9mgezqcczjunl6q0d90hm4d",
                ],
        },
        # BitcoinSV
        {
            "coin"       : Bip44Coins.BITCOIN_SV_TESTNET,
            "names"      : ("BitcoinSV TestNet", "BSV"),
            "is_testnet" : True,
            "seed"       : b"5eb00bbddcf069084889a8ab9155568165f5c453ccb85e70811aaed6f6da5fc19a5ac40b389cd370d086206dec8aa6c43daea6690f20ad3d8d48b2d2ce9e38e4",
            "ex_master"  :  "tprv8ZgxMBicQKsPe5YMU9gHen4Ez3ApihUfykaqUorj9t6FDqy3nP6eoXiAo2ssvpAjoLroQxHqr3R5nE3a5dU3DHTjTgJDd7zrbniJr6nrCzd",
            "wif_master" :  "91mamsLpsPxwA9EnYnWT14Q6o8yrX6npaygFQBDroDVq5dZG3q3",
            "account" :
                {
                    "ex_pub"  : "tpubDC5FSnBiZDMmhiuCmWAYsLwgLYrrT9rAqvTySfuCCrgsWz8wxMXUS9Tb9iVMvcRbvFcAHGkMD5Kx8koh4GquNGNTfohfk7pgjhaPCdXpoba",
                    "ex_priv" : "tprv8fPDJN9UQqg6pFsQsrVxTwHZmXLvHpfGGcsCA9rtnatUgVtBKxhtFeqiyaYKSWydunKpjhvgJf6PwTwgirwuCbFq8YKgpQiaVJf3JCrNmkR",
                },
            "chain_ext" :
                {
                    "ex_pub"  : "tpubDEQBfiy13hMZzGT4NWqNnaSWwVqYQ58kuu2pDYjkrf8F6DLKAprm8c65Pyh7PrzodXHtJuEXFu5yf6JbvYaL8rz7v28zapwbuzZzr7z4UvR",
                    "ex_priv" : "tprv8hi9XJvkuKfu6oRGUsAnPAnQNUKcEjwrLbS2w2hTSPKrFj5YYS3Ax7UDDrZZHd4PSnPLW5whNxAXTW5bBrSNiSD1LUeg9n4j5sdGRJsZZwP",
                },
            "addresses" :
                [
                    "mkpZhYtJu2r87Js3pDiWJDmPte2NRZ8bJV",
                    "mzpbWabUQm1w8ijuJnAof5eiSTep27deVH",
                    "mnTkxhNkgx7TsZrEdRcPti564yQTzynGJp",
                    "mpW3iVi2Td1vqDK8Nfie29ddZXf9spmZkX",
                    "n2BMo5arHDyAK2CM8c56eoEd18uEkKnRLC",
                ],
        },
        # Litecoin test net
        {
            "coin"       : Bip44Coins.LITECOIN_TESTNET,
            "names"      : ("Litecoin TestNet", "LTC"),
            "is_testnet" : True,
            "seed"       : b"5eb00bbddcf069084889a8ab9155568165f5c453ccb85e70811aaed6f6da5fc19a5ac40b389cd370d086206dec8aa6c43daea6690f20ad3d8d48b2d2ce9e38e4",
            "ex_master"  :  "ttpv96BtqegdxXceQk8r9KuoG5yiMACLxANu9hh98NpMwpzcCa8XfrJ7uwnRBMzsE5n9y2exs7VQBBdHNiJ66BrDUWE28WoexgbFVRkRc2abBR9",
            "wif_master" :  "91mamsLpsPxwA9EnYnWT14Q6o8yrX6npaygFQBDroDVq5dZG3q3",
            "account" :
                {
                    "ex_pub"  : "ttub4d4VPcY3DBxKCoAjoeDr9q3FaD4dbY89X65XUhapWiaSFbEjYLwnNg2EcHgEVSEALaEVdZnprREdcWMPJxqFkvN89FcPRFBueauxVCvFpUt",
                    "ex_priv" : "ttpv9Bt9nq7Vy3RMavTuZ2jU5FD38eNSXHZVSZyVoipXaXnqfE3fDRuMN4uyMufJjnb45U7zBs8EdoJbXxCCjRL5Tp27oNq89yJyNwhA48Rqv9P",
                },
            "chain_ext" :
                {
                    "ex_pub"  : "ttub4fPRcZKKhfx7VLibQetg54Y6BA3KYTQjb4eNFaRPAX1oppS6kpH558eirYsyxgoN3qvDfCGzuEzf8qrJBEZgXWynPU3iFxJppsua8eJixXb",
                    "ex_priv" : "ttpv9ED61mtnTXR9sU1mA3QHzUhsjbM8UCr5WYYLabf6ELEDETF2RuEe4XYTcBgYatfocUBVxF9Fi6Nj3zL7CQpYyeyJ1KA7VLf7yWfPB8Cjufb",
                },
            "addresses" :
                [
                    "mkpZhYtJu2r87Js3pDiWJDmPte2NRZ8bJV",
                    "mzpbWabUQm1w8ijuJnAof5eiSTep27deVH",
                    "mnTkxhNkgx7TsZrEdRcPti564yQTzynGJp",
                    "mpW3iVi2Td1vqDK8Nfie29ddZXf9spmZkX",
                    "n2BMo5arHDyAK2CM8c56eoEd18uEkKnRLC",
                ],
        },
        # Dogecoin test net
        {
            "coin"       : Bip44Coins.DOGECOIN_TESTNET,
            "names"      : ("Dogecoin TestNet", "DOGE"),
            "is_testnet" : True,
            "seed"       : b"5eb00bbddcf069084889a8ab9155568165f5c453ccb85e70811aaed6f6da5fc19a5ac40b389cd370d086206dec8aa6c43daea6690f20ad3d8d48b2d2ce9e38e4",
            "ex_master"  :  "tgpv1aRS3XcGkbKXDbWwtRDZFYqUaCsEVXgkHt9m5mEjaWGGA18gaU1qZatwWCmjT66o2CmSNJmXkAvG29sYFXrz11WEaLwVrckr5LMkUrVeQmp",
            "wif_master" :  "95f58LEtaFKPRnQCMwkSuhbedNDHpWUaAFpTtUbenXWc4oSGq5N",
            "account" :
                {
                    "ex_pub"  : "tgub5QziLPy2KFnZgdWALMfCBZcPpFQxtmu3sMDKvDdt1L7WAiAWXpAqf1S9FzNEEa7ipDM6kEy4o9mrVGshjxMKMoq383HELMHguMNGgRryJwt",
                    "ex_priv" : "tgpv1g7gzi38m78EPmr1J83E4i4oMh3L4esLakS7m7EuDD4Vcf3p83d51i2VgkSAxnuh8eETh4QNCnbaBPmetmLqzKJLFCxy3uUZxrJUw2K7GUp",
                },
            "chain_ext" :
                {
                    "ex_pub"  : "tgub5TKeZLkJojnMyB41wNL26o7ERCPeqhBdwKnAh6USf8YsjwMskHW8MU4dWFZyhpgvXV2pmsTEqyXt1cNccE5k8QShNFiZB4Qc5eMtKv6s9mt",
                    "ex_priv" : "tgpv1iSdDepRFb82gKPru8i3ywZdxe221a9veizxXz5Ts1VsBtFBLWxMiAeyw2TQotzSfeHyTSRPH5fhhRuZMkqKWAFWT9HxPGpiZRGi3zY83Mf",
                },
            "addresses" :
                [
                    "nZVmfmUtKPmskB9Ds4P9GUJy9eYFqPKHqH",
                    "noVoUoC3q7wgmb25McqSdLCHhUAhSREkT9",
                    "nb8xvuyL7K3DWS8QgGH2rxcfKyvMQ1wiYe",
                    "ndBFgiJbsywgU5bJRWPGzQBCpYB3M1DZCU",
                    "nprZmJBRhatuwtUXBSjjd3nCG9R8DDm3y3",
                ],
        },
        # Dash test net
        {
            "coin"       : Bip44Coins.DASH_TESTNET,
            "names"      : ("Dash TestNet", "DASH"),
            "is_testnet" : True,
            "seed"       : b"5eb00bbddcf069084889a8ab9155568165f5c453ccb85e70811aaed6f6da5fc19a5ac40b389cd370d086206dec8aa6c43daea6690f20ad3d8d48b2d2ce9e38e4",
            "ex_master"  :  "tprv8ZgxMBicQKsPe5YMU9gHen4Ez3ApihUfykaqUorj9t6FDqy3nP6eoXiAo2ssvpAjoLroQxHqr3R5nE3a5dU3DHTjTgJDd7zrbniJr6nrCzd",
            "wif_master" :  "91mamsLpsPxwA9EnYnWT14Q6o8yrX6npaygFQBDroDVq5dZG3q3",
            "account" :
                {
                    "ex_pub"  : "tpubDC5FSnBiZDMmhiuCmWAYsLwgLYrrT9rAqvTySfuCCrgsWz8wxMXUS9Tb9iVMvcRbvFcAHGkMD5Kx8koh4GquNGNTfohfk7pgjhaPCdXpoba",
                    "ex_priv" : "tprv8fPDJN9UQqg6pFsQsrVxTwHZmXLvHpfGGcsCA9rtnatUgVtBKxhtFeqiyaYKSWydunKpjhvgJf6PwTwgirwuCbFq8YKgpQiaVJf3JCrNmkR",
                },
            "chain_ext" :
                {
                    "ex_pub"  : "tpubDEQBfiy13hMZzGT4NWqNnaSWwVqYQ58kuu2pDYjkrf8F6DLKAprm8c65Pyh7PrzodXHtJuEXFu5yf6JbvYaL8rz7v28zapwbuzZzr7z4UvR",
                    "ex_priv" : "tprv8hi9XJvkuKfu6oRGUsAnPAnQNUKcEjwrLbS2w2hTSPKrFj5YYS3Ax7UDDrZZHd4PSnPLW5whNxAXTW5bBrSNiSD1LUeg9n4j5sdGRJsZZwP",
                },
            "addresses" :
                [
                    "yRd4FhXfVGHXpsuZXPNkMrfD9GVj46pnjt",
                    "yfd64jEpzzTLrHnR1wq3iiYXh68AiU8mcw",
                    "yTGFWr27HBYsb8tkLbGdxLxuKbspamdbnG",
                    "yVJYGeMP3rTLYnMe5qNt5nXSpA8WUTcz49",
                    "ygyrMEECsTQa2bErqmjLiS8SFmNbQ4ynNF",
                ],
        },
    ]

# Tests for different key formats
TEST_VECT_KEY_FORMATS = \
    {
        "coin"            : Bip44Coins.BITCOIN,
        "seed"            : "5eb00bbddcf069084889a8ab9155568165f5c453ccb85e70811aaed6f6da5fc19a5ac40b389cd370d086206dec8aa6c43daea6690f20ad3d8d48b2d2ce9e38e4",
        "ex_priv"         : "xprv9s21ZrQH143K3GJpoapnV8SFfukcVBSfeCficPSGfubmSFDxo1kuHnLisriDvSnRRuL2Qrg5ggqHKNVpxR86QEC8w35uxmGoggxtQTPvfUu",
        "raw_priv"        : "1837c1be8e2995ec11cda2b066151be2cfb48adf9e47b151d46adab3a21cdf67",
        "ex_pub"          : "xpub661MyMwAqRbcFkPHucMnrGNzDwb6teAX1RbKQmqtEF8kK3Z7LZ59qafCjB9eCRLiTVG3uxBxgKvRgbubRhqSKXnGGb1aoaqLrpMBDrVxga8",
        "raw_compr_pub"   : "03d902f35f560e0470c63313c7369168d9d7df2d49bf295fd9fb7cb109ccee0494",
        "raw_uncompr_pub" : "d902f35f560e0470c63313c7369168d9d7df2d49bf295fd9fb7cb109ccee04947d000a1345d3845dd83b4c5814f876c918305b598f066c958fad972bf59f2ec7",
    }

# Tests for extended keys with valid and invalid depths
TEST_VECT_EX_KEY_DEPTHS = \
    {
        # Private key with depth 5 is fine
        "ex_priv_5" : "xprvA47LQAPDXEkr9wwtUHNta4qWqiobTGKppzVy5JZVCszLdGTTQbuRxRMCJGqSdBg91M13Z2RTP2BKU5yDD41WFwZ7yavhhbCEs7cTnyvkxJV",
        # Private key with depth 6 shall raise an exception
        "ex_priv_6" : "xprvA69uJSR3uVgvYFM5AFabGnMuAvtdLrbm84CwEieMBbk5Kjk9ZGeYPF4AWuJ9EPBzC8pLn117Y6TFqgNKZ6EVKmoDxT4EjT1BaG3RhWL6wdF",
        # Public key with depth 2 shall raise an exception
        "ex_pub_2"  : "xpub6AmukNpN4yyLgyzSysjU6JqqoYA1mVUvtinHYdBGPDppatJXHxT8CcDsmBo9n3yLBgrcw9z62ygt1siT9xai4UaJ2w4FPmY6kPCF96YN2cF",
        # Public key with depth 3 shall raise an exception
        "ex_pub_3"  : "xpub6BosfCnifzxcFwrSzQiqu2DBVTshkCXacvNsWGYJVVhhawA7d4R5WSWGFNbi8Aw6ZRc1brxMyWMzG3DSSSSoekkudhUd9yLb6qx39T9nMdj",
        # Public key with depth 5 is fine
        "ex_pub_5"  : "xpub6Fbrwk4KhC8qnFVXTcR3wRsqiTGkedcSSZKyTqKaxXjFN6rZv3UJYZ4mQtjNYY3gCa181iCHSBWyWst2PFiXBKgLpFVSdcyLbHyAahin8pd",
        # Public key with depth 6 shall raise an exception
        "ex_pub_6"  : "xpub6JtuhUVosPSgpBQFZS9oy6oorydcmXS66Kr2TmURvm8uu5wWBXRmRziMT85N4epgkVtwgxpt5FnduVJFi1ARiUcSELWhnZwp9Ge1icYFvhj",
    }

# Tests for coins
TEST_VECT_COINS = \
    {
        "seed"   : b"5eb00bbddcf069084889a8ab9155568165f5c453ccb85e70811aaed6f6da5fc19a5ac40b389cd370d086206dec8aa6c43daea6690f20ad3d8d48b2d2ce9e38e4",
        "ex_key" :  "xprv9s21ZrQH143K3GJpoapnV8SFfukcVBSfeCficPSGfubmSFDxo1kuHnLisriDvSnRRuL2Qrg5ggqHKNVpxR86QEC8w35uxmGoggxtQTPvfUu",

        # Bip44 allows all coins
        "allowed" :
        [
            Bip44Coins.BITCOIN,
            Bip44Coins.LITECOIN,
            Bip44Coins.DOGECOIN,
            Bip44Coins.DASH,
            Bip44Coins.BITCOIN_TESTNET,
            Bip44Coins.LITECOIN_TESTNET,
            Bip44Coins.DOGECOIN_TESTNET,
            Bip44Coins.DASH_TESTNET,
            Bip44Coins.ETHEREUM,
            Bip44Coins.RIPPLE,
        ],
        "not_allowed" :
        [],
    }

# Seed for generic tests that need it
TEST_SEED = b"5eb00bbddcf069084889a8ab9155568165f5c453ccb85e70811aaed6f6da5fc19a5ac40b389cd370d086206dec8aa6c43daea6690f20ad3d8d48b2d2ce9e38e4"

#
# Tests
#
class Bip44Tests(unittest.TestCase):
    # Test specification name
    def test_spec_name(self):
        self.assertEqual(Bip44.SpecName(), "BIP-0044")

    # Run all tests in test vector using FromSeed for construction
    def test_from_seed(self):
        Bip44BaseTestHelper.test_from_seed(self, Bip44, TEST_VECT)

    # Run all tests in test vector using FromExtendedKey for construction
    def test_from_ex_key(self):
        Bip44BaseTestHelper.test_from_ex_key(self, Bip44, TEST_VECT)

    # Test for IsLevel method
    def test_is_level(self):
        Bip44BaseTestHelper.test_is_level(self, Bip44, TEST_SEED)

    # Test different key formats
    def test_key_formats(self):
        Bip44BaseTestHelper.test_key_formats(self, Bip44, TEST_VECT_KEY_FORMATS)

    # Test construction from extended keys with valid and invalid depths
    def test_from_ex_key_depth(self):
        Bip44BaseTestHelper.test_from_ex_key_depth(self, Bip44, TEST_VECT_EX_KEY_DEPTHS)

    # Test coins
    def test_coins(self):
        Bip44BaseTestHelper.test_coins(self, Bip44, TEST_VECT_COINS)

    # Test invalid path derivations
    def test_invalid_derivations(self):
        Bip44BaseTestHelper.test_invalid_derivations(self, Bip44, TEST_SEED)
