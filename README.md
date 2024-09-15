# Skins Price API compare

## Prototype
- code
    - Python/bash
- what will it do
    - Be able to search Skins prices
    - Compare prices between different sites
- What can you search
    - Skins
    - Wear
    - Float
    - Patterns
    - Stattrack
- What will we get out of the prototype
    - Understanding how to search through these APIs
    - What can we do with them ie how specific can we search
    - What other websites or APIs can we use

# Recources
- Steam Docs
    - [Steam api overview](https://partner.steamgames.com/doc/webapi_overview)
    - [Steam Prices](https://partner.steamgames.com/doc/store/pricing/currencies)
    - [ISteamEconomy interface](https://partner.steamgames.com/doc/webapi/ISteamEconomy)
## API
- Steam
    - [Steam API](https://steamcommunity.com/market/priceoverview/?appid=730&currency=2&market_hash_name=M4A1-S%20|%20Golden%20Coil%20(Minimal%20Wear))
        - GetMarketPrices
            - GET https://partner.steam-api.com/ISteamEconomy/GetMarketPrices/v1/
                - key	string	✔	Steamworks Web API publisher authentication key.
                - appid	uint32	✔	Must be a steam economy app.