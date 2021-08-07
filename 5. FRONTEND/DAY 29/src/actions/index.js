const UpdatePlace = (place) => {
    return {
        type : "UPDATE_PLACE",
        payload: place,
    }
}

const UpdatePlaceData = (place) => {
    return(dispatch) => {
        fetch(`https://api.weatherapi.com/v1/current.json?key=decd753b07014de186b155610213007&q=${place}&aqi=no`
    )
    .then((resp) => resp.json())
    .then((data) => {
        dispatch({
            type: "UPDATE_PLACE_DATA",
            payload: data,
        });
    })
    .catch((e) => {
        return place;
    });
      }
}

const ToggleTheme = () => {
    return {
        type : "TOGGLE_THEME",
    }
}
export {UpdatePlace,UpdatePlaceData,ToggleTheme};