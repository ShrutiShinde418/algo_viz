import React from "react";
import MainLayout from "./MainLayout";
import Sidebar from "./SideBar";

class App extends React.Component {
  render() {
    return (
      <div>
        <MainLayout />
        <Sidebar />
      </div>
    );
  }
}

export default App;
