
def validate_channel_consistency(df):
    
    # Check order count consistency
    df["Total_Channel_orders"] = (
        df["InStoreOrders"] +
        df["UberEatsOrders"] +
        df["DoorDashOrders"] +
        df["SelfDeliveryOrders"]
    )
    
    df["Order_Mismatch"] = df["MonthlyOrders"] - df["Total_Channel_Orders"]
    
    # Check share consistency
    df["Total_Share"] = (
        df["InStoreShare"] +
        df["UE_share"] +
        df["DD_share"] +
        df["SD_share"]
    )
    
    df["Share_Mismatch"] = df["Total_Share"] - 100
    
    return df