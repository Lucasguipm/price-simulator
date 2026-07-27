import random
from datetime import datetime, timedelta

def generate_price_history(current_price):
    """
    Gera um histórico temporário realista de 90 dias 
    com flutuações percentuais em torno do preço atual real.
    """
    now = datetime.now()
    history = []

    # Cria dados retroativos de 90 dias atrás até hoje
    for i in range(90, -1, -1):
        date_str = (now - timedelta(days=i)).strftime("%Y-%m-%d")
        
        # Simula variações entre -8% e +8%
        variation = random.uniform(-0.08, 0.08)
        simulated_price = round(current_price * (1 + variation), 2)
        
        history.append({
            "date": date_str,
            "price": simulated_price
        })

    # Garante que a data de hoje reflita exatamente o preço raspado no momento
    history[-1]["price"] = current_price

    return {
        "7_days": history[-8:],
        "30_days": history[-31:],
        "90_days": history
    }