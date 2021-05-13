#pip install cryptocompare
import cryptocompare

try:
    print("""
    AUR - Auroracoin
    BCC - BitConnect (inactive)
    BCH - Bitcoin Cash
    BTC or XBT - Bitcoin
    DASH - Dash
    DOGE or XDG - Dogecoin
    EOS - EOS.IO
    ETC - Ethereum Classic
    ETH - Ether (also known as Ethereum)
    GRC - Gridcoin
    LTC - Litecoin
    KOI or COYE - Coinye (inactive)
    MZC - Mazacoin
    Nano - Nano
    NEO - Neo
    NMC - Namecoin
    Nxt - NXT
    POT - PotCoin
    PPC - Peercoin
    TIT - Titcoin
    USDC - USD Coin (stablecoin)
    USDT - Tether
    VTC - Vertcoin
    XEM - NEM
    XLM - Stellar
    XMR - Monero
    XPM - Primecoin
    XRP - Ripple
    XVG - Verge
    ZEC - Zcash
    """)

    currency = input("Enter the Crypto Currency : ")

    coin_usd = cryptocompare.get_price(currency, currency='USD')

    coin_eur = cryptocompare.get_price(currency, currency='EUR')

    print("Price of one ", currency, " in USD = ", coin_usd)
    print("Price of one ", currency, " in EUR = ", coin_eur)
except:
    print("Error occurred in the execution. try again!!")
