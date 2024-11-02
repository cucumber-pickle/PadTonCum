import requests
import json
import os
from core.helper import get_headers, countdown_timer, extract_user_data, config
from colorama import *
import random
from datetime import datetime, timedelta, timezone
import time
import pytz


class PadTON:
    def __init__(self) -> None:
        self.session = requests.Session()


    def clear_terminal(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def log(self, message):
        print(
            f"{Fore.CYAN + Style.BRIGHT}[ {datetime.now().strftime('%x %X %Z')} ]{Style.RESET_ALL}"
            f"{Fore.WHITE + Style.BRIGHT} | {Style.RESET_ALL}{message}",
            flush=True
        )

    def welcome(self):
        banner = f"""{Fore.GREEN}
                                         ██████  ██    ██   ██████  ██    ██  ███    ███  ██████   ███████  ██████  
                                        ██       ██    ██  ██       ██    ██  ████  ████  ██   ██  ██       ██   ██ 
                                        ██       ██    ██  ██       ██    ██  ██ ████ ██  ██████   █████    ██████  
                                        ██       ██    ██  ██       ██    ██  ██  ██  ██  ██   ██  ██       ██   ██ 
                                         ██████   ██████    ██████   ██████   ██      ██  ██████   ███████  ██   ██     
                                            """
        print(Fore.GREEN + Style.BRIGHT + banner + Style.RESET_ALL)
        print(Fore.GREEN + f" PadTON Bot")
        print(Fore.RED + f" FREE TO USE = Join us on {Fore.GREEN}t.me/cucumber_scripts")
        print(Fore.YELLOW + f" before start please '{Fore.GREEN}git pull{Fore.YELLOW}' to update bot")
        print(f"{Fore.WHITE}~" * 60)

    def format_seconds(self, seconds):
        hours, remainder = divmod(seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        return f"{int(hours):02}:{int(minutes):02}:{int(seconds):02}"

    def auth_signin(self, query: str):
        url = 'https://api-community-miniapp.padton.com/api/auth/signin-with-telegram-miniapp'
        data = json.dumps({"initData":query})
        self.headers.update({
            'Content-Type': 'application/json'
        })

        response = self.session.post(url, headers=self.headers, data=data)
        result = response.json()
        if result['status']:
            return result['data']['accessToken']
        else:
            return None
        
    def users_me(self, token: str):
        url = 'https://api-community-miniapp.padton.com/api/users/me'
        self.headers.update({
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'
        })

        response = self.session.get(url, headers=self.headers)
        result = response.json()
        if result['status']:
            return result['data']
        else:
            return None
        
    def loyality_wallet(self, token: str):
        url = 'https://api-community-miniapp.padton.com/api/loyalty-wallet'
        self.headers.update({
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'
        })

        response = self.session.get(url, headers=self.headers)
        result = response.json()
        if result['status']:
            return result['data']
        else:
            return None
        
    def entry_requirements(self, token: str):
        url = 'https://api-community-miniapp.padton.com/api/entry-requirements/my-list'
        self.headers.update({
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'
        })

        response = self.session.get(url, headers=self.headers)
        result = response.json()
        if result['status']:
            return result['data']
        else:
            return None
        
    def verify_requirements(self, token: str, require_id: str):
        url = f'https://api-community-miniapp.padton.com/api/entry-requirements/{require_id}/verify'
        data = {}
        self.headers.update({
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'
        })

        response = self.session.post(url, headers=self.headers, json=data)
        result = response.json()
        if result['status']:
            return result['data']
        else:
            return None
        
    def notifications(self, token: str):
        url = 'https://api-community-miniapp.padton.com/api/notifications?isRead=false'
        self.headers.update({
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'
        })

        response = self.session.get(url, headers=self.headers)
        result = response.json()
        if result['status']:
            return result['data']
        else:
            return None
        
    def read_notifications(self, token: str):
        url = 'https://api-community-miniapp.padton.com/api/notifications/read'
        data = {}
        self.headers.update({
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'
        })

        response = self.session.patch(url, headers=self.headers, json=data)
        result = response.json()
        if result['status']:
            return result['data']
        else:
            return None
        
    def farm_pool(self, token: str):
        url = 'https://api-community-miniapp.padton.com/api/farm-pool/current'
        self.headers.update({
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'
        })

        response = self.session.get(url, headers=self.headers)
        result = response.json()
        if result['status']:
            return result['data']
        else:
            return None
        
    def start_farm(self, token: str):
        url = 'https://api-community-miniapp.padton.com/api/farm-pool'
        data = {}
        self.headers.update({
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'
        })

        response = self.session.post(url, headers=self.headers, json=data)
        result = response.json()
        if result['status']:
            return result['data']
        else:
            return None

    def claim_farm(self, token: str, farm_id: str):
        url = f'https://api-community-miniapp.padton.com/api/farm-pool/{farm_id}/claim'
        data = {}
        self.headers.update({
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'
        })

        response = self.session.patch(url, headers=self.headers, json=data)
        result = response.json()
        if result['status']:
            return result['data']
        else:
            return None
        
    def lucky_spin(self, token: str):
        url = 'https://api-community-miniapp.padton.com/api/lucky-spin/profile'
        self.headers.update({
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'
        })

        response = self.session.get(url, headers=self.headers)
        result = response.json()
        if result['status']:
            return result['data']
        else:
            return None
        
    def spin_wheel(self, token: str):
        url = 'https://api-community-miniapp.padton.com/api/lucky-spin/spin'
        data = {}
        self.headers.update({
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'
        })

        response = self.session.post(url, headers=self.headers, json=data)
        result = response.json()
        if result['status']:
            return result['data']
        else:
            return None
        
    def missions(self, token: str):
        url = 'https://api-community-miniapp.padton.com/api/missions'
        self.headers.update({
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'
        })

        response = self.session.get(url, headers=self.headers)
        result = response.json()
        if result['status']:
            return result['data']
        else:
            return None
        
    def start_missions(self, token: str, mission_id: str):
        url = f'https://api-community-miniapp.padton.com/api/missions/{mission_id}/start'
        data = {}
        self.headers.update({
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'
        })

        response = self.session.patch(url, headers=self.headers, json=data)
        result = response.json()
        if result['status']:
            return result['data']
        else:
            return None
        
    def claim_missions(self, token: str, mission_id: str):
        url = f'https://api-community-miniapp.padton.com/api/missions/{mission_id}/claim'
        data = {}
        self.headers.update({
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'
        })

        response = self.session.patch(url, headers=self.headers, json=data)
        result = response.json()
        if result['status']:
            return result['data']
        else:
            return None

    def connect_wallet(self, token: str, wallet: str):
        url = 'https://api-community-miniapp.padton.com/api/users/link-wallet'
        data = json.dumps({'walletAddress': wallet})
        self.headers.update({
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'
        })
        try:
            response = self.session.patch(url, headers=self.headers, data=data)

            if response.status_code == 200:
                response.raise_for_status()
                result = response.json()
                if result and result.get('message') == "Successfully":
                    self.log(Fore.GREEN + f'Successfully connected to wallet')
            else:
                self.log(response.text)
                self.log(Fore.RED + f"Failed connecting wallet")

        except Exception as e:
            self.log(e)
            self.log(Fore.RED + f"Failed connecting wallet")

    def set_proxy(self, proxy):
        self.session.proxies = {
            "http": proxy,
            "https": proxy,
        }
        if '@' in proxy:
            host_port = proxy.split('@')[-1]
        else:
            host_port = proxy.split('//')[-1]
        return host_port

    def process_query(self, query: str, wallet_connect:str):

        token = self.auth_signin(query)
        if not token:
            self.log(
                f"{Fore.MAGENTA+Style.BRIGHT}[ Account{Style.RESET_ALL}"
                f"{Fore.RED+Style.BRIGHT} Query Isn't Valid {Style.RESET_ALL}"
                f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
            )
            return
        
        if token:

            if wallet_connect:
                self.connect_wallet(token, wallet_connect)
                time.sleep(1)


            wallet = self.loyality_wallet(token)
            if wallet:
                user = self.users_me(token)
                if user:
                    self.log(
                        f"{Fore.MAGENTA+Style.BRIGHT}[ Account{Style.RESET_ALL}"
                        f"{Fore.WHITE+Style.BRIGHT} {user['firstName']} {Style.RESET_ALL}"
                        f"{Fore.MAGENTA+Style.BRIGHT}] [ Balance{Style.RESET_ALL}"
                        f"{Fore.WHITE+Style.BRIGHT} {wallet['totalBalance']} PATC {Style.RESET_ALL}"
                        f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                    )
                else:
                    self.log(
                        f"{Fore.MAGENTA+Style.BRIGHT}[ Account{Style.RESET_ALL}"
                        f"{Fore.RED+Style.BRIGHT} Token Is None {Style.RESET_ALL}"
                        f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                    )
            else:
                self.log(
                    f"{Fore.MAGENTA+Style.BRIGHT}[ Account{Style.RESET_ALL}"
                    f"{Fore.RED+Style.BRIGHT} Token Is None {Style.RESET_ALL}"
                    f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                )
            time.sleep(1)

            requirements = self.entry_requirements(token)
            if requirements:
                for require in requirements:
                    require_id = require['id']
                    status = require['status']

                    if require and status == 'PENDING':
                        verify = self.verify_requirements(token, require_id)
                        if verify and verify['status'] == 'SUCCESS':
                            self.log(
                                f"{Fore.MAGENTA+Style.BRIGHT}[ Verify{Style.RESET_ALL}"
                                f"{Fore.WHITE+Style.BRIGHT} {verify['code']} {Style.RESET_ALL}"
                                f"{Fore.GREEN+Style.BRIGHT}Is Success{Style.RESET_ALL}"
                                f"{Fore.MAGENTA+Style.BRIGHT} ] [ Reward{Style.RESET_ALL}"
                                f"{Fore.WHITE+Style.BRIGHT} {verify['info']['reward']} PATC {Style.RESET_ALL}"
                                f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                            )
                        else:
                            self.log(
                                f"{Fore.MAGENTA+Style.BRIGHT}[ Verify{Style.RESET_ALL}"
                                f"{Fore.WHITE+Style.BRIGHT} {verify['code']} {Style.RESET_ALL}"
                                f"{Fore.RED+Style.BRIGHT}Isn't Success{Style.RESET_ALL}"
                                f"{Fore.MAGENTA+Style.BRIGHT} ]{Style.RESET_ALL}"
                            )
                        time.sleep(1)
            else:
                self.log(
                    f"{Fore.MAGENTA+Style.BRIGHT}[ Account{Style.RESET_ALL}"
                    f"{Fore.YELLOW+Style.BRIGHT} Is Already Required {Style.RESET_ALL}"
                    f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                )
            time.sleep(1)


            notifications = self.notifications(token)
            if notifications:
                self.read_notifications(token)


            farm = self.farm_pool(token)
            if farm is None:
                start = self.start_farm(token)
                if start:
                    end_at = datetime.strptime(start['estimatedEndAt'], "%Y-%m-%dT%H:%M:%S.%fZ").replace(tzinfo=pytz.utc)
                    end_at_wib = end_at.strftime('%x %X %Z')
                    self.log(
                        f"{Fore.MAGENTA+Style.BRIGHT}[ Farming{Style.RESET_ALL}"
                        f"{Fore.GREEN+Style.BRIGHT} Is Started {Style.RESET_ALL}"
                        f"{Fore.MAGENTA+Style.BRIGHT}] [ Claim at{Style.RESET_ALL}"
                        f"{Fore.WHITE+Style.BRIGHT} {end_at_wib} {Style.RESET_ALL}"
                        f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                    )
                else:
                    self.log(
                        f"{Fore.MAGENTA+Style.BRIGHT}[ Farming{Style.RESET_ALL}"
                        f"{Fore.RED+Style.BRIGHT} Isn't Started {Style.RESET_ALL}"
                        f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                    )
                time.sleep(1)

                farm = self.farm_pool(token)

            if farm:
                farm_id = farm['id']

                end_at = datetime.strptime(farm['estimatedEndAt'], "%Y-%m-%dT%H:%M:%S.%fZ").replace(tzinfo=pytz.utc)
                end_at_wib = end_at.strftime('%x %X %Z')

                now_utc = datetime.now(timezone.utc)

                if now_utc >= end_at:
                    claim = self.claim_farm(token, farm_id)
                    if claim:
                        self.log(
                            f"{Fore.MAGENTA+Style.BRIGHT}[ Farming{Style.RESET_ALL}"
                            f"{Fore.GREEN+Style.BRIGHT} Is Claimed {Style.RESET_ALL}"
                            f"{Fore.MAGENTA+Style.BRIGHT}] [ Reward{Style.RESET_ALL}"
                            f"{Fore.WHITE+Style.BRIGHT} {claim['loyaltyAmount']} PATC {Style.RESET_ALL}"
                            f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                        )
                    else:
                        self.log(
                            f"{Fore.MAGENTA+Style.BRIGHT}[ Farming{Style.RESET_ALL}"
                            f"{Fore.YELLOW+Style.BRIGHT} Is Already Claimed {Style.RESET_ALL}"
                            f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                        )
                    time.sleep(1)

                    start = self.start_farm(token)
                    if start:
                        end_at = datetime.strptime(start['estimatedEndAt'], "%Y-%m-%dT%H:%M:%S.%fZ").replace(tzinfo=pytz.utc)
                        end_at_wib = end_at.strftime('%x %X %Z')
                        self.log(
                            f"{Fore.MAGENTA+Style.BRIGHT}[ Farming{Style.RESET_ALL}"
                            f"{Fore.GREEN+Style.BRIGHT} Is Started {Style.RESET_ALL}"
                            f"{Fore.MAGENTA+Style.BRIGHT}] [ Claim at{Style.RESET_ALL}"
                            f"{Fore.WHITE+Style.BRIGHT} {end_at_wib} {Style.RESET_ALL}"
                            f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                        )
                    else:
                        self.log(
                            f"{Fore.MAGENTA+Style.BRIGHT}[ Farming{Style.RESET_ALL}"
                            f"{Fore.RED+Style.BRIGHT} Isn't Started {Style.RESET_ALL}"
                            f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                        )
                else:
                    self.log(
                        f"{Fore.MAGENTA+Style.BRIGHT}[ Farming{Style.RESET_ALL}"
                        f"{Fore.YELLOW+Style.BRIGHT} Not Time to Claim {Style.RESET_ALL}"
                        f"{Fore.MAGENTA+Style.BRIGHT}] [ Claim at{Style.RESET_ALL}"
                        f"{Fore.WHITE+Style.BRIGHT} {end_at_wib} {Style.RESET_ALL}"
                        f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                    )
                time.sleep(1)

            lucky_spin = self.lucky_spin(token)
            if lucky_spin:
                count = lucky_spin['totalSpin']
                while count > 0:
                    spin = self.spin_wheel(token)
                    if spin:
                        reward = spin['amount']
                        symbol = spin['currencySymbol']
                        self.log(
                            f"{Fore.MAGENTA+Style.BRIGHT}[ Lucky Spin{Style.RESET_ALL}"
                            f"{Fore.GREEN+Style.BRIGHT} Is Success {Style.RESET_ALL}"
                            f"{Fore.MAGENTA+Style.BRIGHT}] [ Reward{Style.RESET_ALL}"
                            f"{Fore.WHITE+Style.BRIGHT} {reward} {symbol} {Style.RESET_ALL}"
                            f"{Fore.MAGENTA+Style.BRIGHT}] [ Chances{Style.RESET_ALL}"
                            f"{Fore.WHITE+Style.BRIGHT} {count-1} Left {Style.RESET_ALL}"
                            f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                        )
                        count -= 1
                        time.sleep(1)
                    else:
                        break

                if count == 0:
                    self.log(
                        f"{Fore.MAGENTA+Style.BRIGHT}[ Lucky Spin{Style.RESET_ALL}"
                        f"{Fore.YELLOW+Style.BRIGHT} No Available Chance {Style.RESET_ALL}"
                        f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                    )
            else:
                self.log(
                    f"{Fore.MAGENTA+Style.BRIGHT}[ Lucky Spin{Style.RESET_ALL}"
                    f"{Fore.RED+Style.BRIGHT} Is None {Style.RESET_ALL}"
                    f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                )
            time.sleep(1)

            missions = self.missions(token)
            if missions:
                for mission in missions:
                    mission_id = mission['id']
                    status = mission['status']

                    if mission and status == 'INIT':
                        start = self.start_missions(token, mission_id)
                        if start and start['status'] == 'PENDING':
                            self.log(
                                f"{Fore.MAGENTA+Style.BRIGHT}[ Task{Style.RESET_ALL}"
                                f"{Fore.WHITE+Style.BRIGHT} {mission['name']} {Style.RESET_ALL}"
                                f"{Fore.GREEN+Style.BRIGHT}Is Started{Style.RESET_ALL}"
                                f"{Fore.MAGENTA+Style.BRIGHT} ]{Style.RESET_ALL}"
                            )
                            time.sleep(3)

                            claim = self.claim_missions(token, mission_id)
                            if claim and claim['status'] == 'SUCCESS':
                                self.log(
                                    f"{Fore.MAGENTA+Style.BRIGHT}[ Task{Style.RESET_ALL}"
                                    f"{Fore.WHITE+Style.BRIGHT} {mission['name']} {Style.RESET_ALL}"
                                    f"{Fore.GREEN+Style.BRIGHT}Is Claimed{Style.RESET_ALL}"
                                    f"{Fore.MAGENTA+Style.BRIGHT} ] [ Reward{Style.RESET_ALL}"
                                    f"{Fore.WHITE+Style.BRIGHT} {mission['loyaltyReward']} PATC {Style.RESET_ALL}"
                                    f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                                )
                            else:
                                self.log(
                                    f"{Fore.MAGENTA+Style.BRIGHT}[ Task{Style.RESET_ALL}"
                                    f"{Fore.WHITE+Style.BRIGHT} {mission['name']} {Style.RESET_ALL}"
                                    f"{Fore.RED+Style.BRIGHT}Isn't Claimed{Style.RESET_ALL}"
                                    f"{Fore.MAGENTA+Style.BRIGHT} ]{Style.RESET_ALL}"
                                )
                        else:
                            self.log(
                                f"{Fore.MAGENTA+Style.BRIGHT}[ Task{Style.RESET_ALL}"
                                f"{Fore.WHITE+Style.BRIGHT} {mission['name']} {Style.RESET_ALL}"
                                f"{Fore.RED+Style.BRIGHT}Isn't Started{Style.RESET_ALL}"
                                f"{Fore.MAGENTA+Style.BRIGHT} ]{Style.RESET_ALL}"
                            )
                        time.sleep(2)

                    elif mission and status == 'PENDING':
                        claim = self.claim_missions(token, mission_id)
                        if claim:
                            self.log(
                                f"{Fore.MAGENTA+Style.BRIGHT}[ Task{Style.RESET_ALL}"
                                f"{Fore.WHITE+Style.BRIGHT} {mission['name']} {Style.RESET_ALL}"
                                f"{Fore.GREEN+Style.BRIGHT}Is Claimed{Style.RESET_ALL}"
                                f"{Fore.MAGENTA+Style.BRIGHT} ] [ Reward{Style.RESET_ALL}"
                                f"{Fore.WHITE+Style.BRIGHT} {mission['loyaltyReward']} PATC {Style.RESET_ALL}"
                                f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                            )
                        else:
                            self.log(
                                f"{Fore.MAGENTA+Style.BRIGHT}[ Task{Style.RESET_ALL}"
                                f"{Fore.WHITE+Style.BRIGHT} {mission['name']} {Style.RESET_ALL}"
                                f"{Fore.RED+Style.BRIGHT}Isn't Claimed{Style.RESET_ALL}"
                                f"{Fore.MAGENTA+Style.BRIGHT} ]{Style.RESET_ALL}"
                            )
                        time.sleep(2)

            else:
                self.log(
                    f"{Fore.MAGENTA+Style.BRIGHT}[ Task{Style.RESET_ALL}"
                    f"{Fore.RED+Style.BRIGHT} Token Is None {Style.RESET_ALL}"
                    f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                )

    def main(self):
        try:
            with open('query.txt', 'r') as file:
                queries = [line.strip() for line in file if line.strip()]
            with open('proxies.txt', 'r') as file:
                proxies = [line.strip() for line in file if line.strip()]
            with open('wallets.txt', 'r') as file:
                wallets = [line.strip() for line in file if line.strip()]

            while True:

                self.log(
                    f"{Fore.GREEN + Style.BRIGHT}Account's Total: {Style.RESET_ALL}"
                    f"{Fore.WHITE + Style.BRIGHT}{len(queries)}{Style.RESET_ALL}"
                )
                self.log(
                    f"{Fore.GREEN + Style.BRIGHT}Proxy's Total: {Style.RESET_ALL}"
                    f"{Fore.WHITE + Style.BRIGHT}{len(proxies)}{Style.RESET_ALL}"
                )
                self.log(
                    f"{Fore.GREEN + Style.BRIGHT}Wallets's Total: {Style.RESET_ALL}"
                    f"{Fore.WHITE + Style.BRIGHT}{len(wallets)}{Style.RESET_ALL}"
                )
                self.log(f"{Fore.CYAN + Style.BRIGHT}-----------------------------------------------------------------------{Style.RESET_ALL}")

                for i, query in enumerate(queries):
                    query = query.strip()
                    if query:
                        self.log(
                            f"{Fore.GREEN + Style.BRIGHT}Account: {Style.RESET_ALL}"
                            f"{Fore.WHITE + Style.BRIGHT}{i + 1} / {len(queries)}{Style.RESET_ALL}"
                        )
                        if len(proxies) >= len(queries):
                            proxy = self.set_proxy(proxies[i])  # Set proxy for each account
                            self.log(
                                f"{Fore.GREEN + Style.BRIGHT}Use proxy: {Style.RESET_ALL}"
                                f"{Fore.WHITE + Style.BRIGHT}{proxy}{Style.RESET_ALL}"
                            )

                        else:
                            self.log(
                                Fore.RED + "Number of proxies is less than the number of accounts. Proxies are not used!")

                        if config['connect_wallets']:
                            if len(wallets) >= len(queries):
                                wallet = wallets[i]
                                self.log(
                                    f"{Fore.GREEN + Style.BRIGHT}Connect wallet:{Style.RESET_ALL}"
                                    f"{Fore.WHITE + Style.BRIGHT}{wallet}{Style.RESET_ALL}"
                                )

                            else:
                                self.log(
                                    Fore.RED + "The number of wallets is less than the number of accounts. The connection of wallets is disabled!")
                                wallet = None
                        else:
                            wallet = None

                        user_info = extract_user_data(query)
                        user_id = str(user_info.get('id'))
                        self.headers = get_headers(user_id)

                        try:
                            self.process_query(query, wallet)
                        except Exception as e:
                            self.log(f"{Fore.RED + Style.BRIGHT}An error process_query: {e}{Style.RESET_ALL}")

                        self.log(f"{Fore.CYAN + Style.BRIGHT}-{Style.RESET_ALL}" * 75)
                        account_delay = config['account_delay']
                        countdown_timer(random.randint(min(account_delay), max(account_delay)))

                cycle_delay = config['cycle_delay']
                countdown_timer(random.randint(min(cycle_delay), max(cycle_delay)))

        except KeyboardInterrupt:
            self.log(f"{Fore.RED + Style.BRIGHT}[ EXIT ] PadTON - BOT{Style.RESET_ALL}")
        except Exception as e:
            self.log(f"{Fore.RED + Style.BRIGHT}An error occurred: {e}{Style.RESET_ALL}")

if __name__ == "__main__":
    bot = PadTON()
    bot.clear_terminal()
    bot.welcome()
    bot.main()