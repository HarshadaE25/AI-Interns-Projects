
def calculate_kpis(df):
    
    total_orders = df["MonthlyOrders"].sum()
    
    channel_totals = {
        "InStore": df["InStoreOrders"].sum(),
        "UberEats": df["UberEatsOrders"].sum(),
        "DoorDash": df["DoorDashOrders"].sum(),
        "SelfDelivery": df["SelfDeliveryOrders"].sum(),
    }
    
    channel_share = {
        key: (value / total_orders) * 100
        for key, value in channel_totals.items()
    }
    
    return total_orders, channel_totals, channel_share