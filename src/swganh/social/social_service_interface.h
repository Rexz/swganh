// This file is part of SWGANH which is released under the MIT license.
// See file LICENSE or go to http://swganh.com/LICENSE
#pragma once

#include <cstdint>
#include <map>
#include <memory>

#include "swganh/service/service_interface.h"

#include "swganh/app/swganh_kernel.h"
#include "swganh/object/object_controller.h"

namespace swganh {
namespace object {
    class Object;
namespace player {
    class Player;
}
}}  // namespace swganh::object

namespace swganh {
namespace character {
class CharacterProviderInterface;
}} // namespace swganh::character

namespace swganh {
namespace social {
    
    class SocialServiceInterface : public anh::service::ServiceInterface
    {
    public:
        
        virtual bool AddFriend(const std::shared_ptr<swganh::object::player::Player>& player, const std::string& friend_name) = 0;
        
		virtual bool AddIgnore(const std::shared_ptr<swganh::object::player::Player>& player, const std::string& player_name) = 0;
        
    };

}}  // namespace swganh::social
