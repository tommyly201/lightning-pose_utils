
def get_col_names(keypoint: str, coordinate: str, models: List[str]) -> List[str]:
    return [get_full_name(keypoint, coordinate, model) for model in models]

    # -------------------------------------------------------------
    # get_col_names
    # -------------------------------------------------------------
def plot_precomputed_traces(df_metrics, df_traces, cols):
    # -------------------------------------------------------------
    # setup
    # -------------------------------------------------------------
    coordinate = "x"  # placeholder
    keypoint = cols[0].split("_%s_" % coordinate)[0]
    colors = px.colors.qualitative.Plotly

    rows = 3
    row_heights = [2, 2, 0.75]
    if temp_norm_error_key in df_metrics.keys():
        rows += 1
        row_heights.insert(0, 0.75)
    if pcamv_error_key in df_metrics.keys():
        rows += 1
        row_heights.insert(0, 0.75)
    if pcasv_error_key in df_metrics.keys():
        rows += 1
        row_heights.insert(0, 0.75)

    fig_traces = make_subplots(
        rows=rows,
        cols=1,
        shared_xaxes=True,
        x_title="Frame number",
        row_heights=row_heights,
        vertical_spacing=0.03,
    )

    yaxis_labels = {}
    row = 1

# ---------------------------------------------------
# plot traces
# ---------------------------------------------------
st.header("Trace diagnostics")

col10, col11 = st.columns(2)

with col10:
    models = st.multiselect(
        "Models:",
        pd.Series(list(dframes_metrics.keys())),
        default=list(dframes_metrics.keys()),
    )

with col11:
    keypoint = st.selectbox("Keypoint:", pd.Series(keypoint_names))

cols = get_col_names(keypoint, "x", models)
fig_traces = plot_precomputed_traces(df_metrics, df_concat, cols)
st.plotly_chart(fig_traces)
