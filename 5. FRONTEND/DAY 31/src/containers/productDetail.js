import React,{useEffect} from 'react';
import axios from 'axios';
import { useParams } from 'react-router-dom';
import {useSelector,useDispatch } from 'react-redux';
import { selectedProduct, removeSelectedProduct} from "../redux/actions/productActions";

const ProductDetails = () => {
    const {productId} = useParams();
    const dispatch = useDispatch();
    const products = useSelector(state => state.selectedProduct);
    // console.log(productId);
    const fetchProdcutDetails = async () => {
        const resp = await axios.get(`https://fakestoreapi.com/products/${productId}`).catch(err => console.log(err))
        dispatch(selectedProduct(resp.data));
    }
    useEffect(() => {
        if(productId && productId !== ""){
            fetchProdcutDetails()
        }
        return () => { dispatch(removeSelectedProduct())};
    },[productId]);
    return (
        <div className="ui grid container">
            {Object.keys(products).length === 0 ?(<div>Loading...</div>)
            :
            (

            <div className="ui placeholder segment">
                <div className="ui two column stakable center aligned grid">
                    <div className="ui vertical divider">AND</div>
                    <div className="middle aligned row">
                        <div className="column lp">
                            <img className="ui fluid image" src={products.image}/>
                        </div>
                        <div className="column rp">
                            <h1>{products.title}</h1>
                            <h2>
                                <a className="ui teal tag label">{products.price}</a>
                            </h2>
                                    <h3 className="ui brown block header">{products.category}</h3>
                                    <p>{products.description}</p>
                                    <div className="ui vertical animated button" tabIndex="0">
                                        <div className="hidden content">
                                            <i className="shop icon"></i>
                                        </div>
                                        <div className="visible content"> Add to Cart </div>
                                    </div>
                        </div>
                    </div>
                </div>
            </div>
            )}
        </div>
    )
}

export default ProductDetails;