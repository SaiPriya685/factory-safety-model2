import { ShieldAlert } from "lucide-react";

function Navbar() {
    return (
        <nav className="navbar">
            <div className="logo">
                <ShieldAlert size={28} />
                <span>AI Factory Safety Copilot</span>
            </div>

            <div className="user">
                👤 Admin
            </div>
        </nav>
    );
}

export default Navbar;