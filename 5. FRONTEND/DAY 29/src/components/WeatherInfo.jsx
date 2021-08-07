import {useSelector} from "react-redux";

const WeatherInfo = () => {
    const theme = useSelector(state => state.theme);
    const placeData = useSelector(store => store.placeData);
    console.log(placeData);
    return (<div className={`WeatherInfo ${theme ? ("") : "dark"}`}>
        
            {placeData.location?
            (<>
            
            <div className="weatherData">
                    <img src={placeData.current.condition.icon}/>
            </div>
            <div className="weatherData">
                <h1>{placeData.current.temp_c}⁰C</h1>
                <div>{placeData.current.condition.text}</div>
                <h3>{placeData.location.name}</h3>
            </div>
            <div className="weatherData">
                    <div className="weatherData-3">
                        <div>Wind Now</div>
                        <div>{placeData.current.wind_kph}<span>KPH</span></div>
                    </div>
                    <div className="weatherData-3">
                        <div>Humidity</div>
                        <div>{placeData.current.humidity}<span>%</span></div>
                    </div>
                    <div className="weatherData-3">
                        <div>Precipitation</div>
                        <div>{placeData.current.precip_mm}<span>%</span></div>
                    </div>
            </div>
            </>)
        :(<>Place Not Found</>)
        }

    </div>);
}

export default WeatherInfo;