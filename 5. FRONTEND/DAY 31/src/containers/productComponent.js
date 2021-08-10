import React from 'react';
import { useSelector } from 'react-redux';
import {Link} from 'react-router-dom';


const ProductComponent = () => {
    const products = useSelector(state => state.allProducts.products);
    // console.log(products);
    const RenderList = products.map(product =>{
        return(
            <div className="four wide column" key={product.id}>
                <Link to={`/product/${product.id}`}>
                <div className="ui link cards">
                    <div className="card abhay-card">
                        <div className="image">
                            <img src={product.image}/>
                        </div>
                        <div className="content">
                            <div className="header"><b>{product.title}</b></div>
                            <div className="meta-price">$ {product.price}</div>
                            <div className="meta">{product.description}</div>
                        </div>
                    </div>
                </div>
                </Link>
            </div>
        );
    })
    return (<>
    {RenderList}
        </>)
}

export default ProductComponent;